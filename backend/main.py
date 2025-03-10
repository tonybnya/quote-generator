from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

import crud
import models
import schemas
from models import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# allow all origins
origins = [
    # allows all origins
    # "*",
    # my frontend
    "https://tonybnya-quote-generator.onrender.com",
    # For local development
    "http://localhost:5173",
]

# Add CORSMiddleware to your FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Or specify a list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


# dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/api")
def read_base():
    return {
        "message": "Welcome to the Quote API!",
        "description": "This API provides a collection of inspirational and motivational quotes.",
        "available_endpoints": {
            "/api/quotes": "Get all the available quotes.",
            "/api/quotes/{id}": "Get a specific quote.",
            "/api/quotes/random": "Get a random quote.",
        },
        "contact": "For support, reach out to tonybnya@gmail.com",
    }


@app.post("/api/quotes/", response_model=schemas.Quote)
def create_quote(quote: schemas.QuoteCreate, db: Session = Depends(get_db)):
    return crud.create_quote(db=db, quote=quote)


@app.get("/api/quotes/random", response_model=schemas.Quote)
def read_random_quote(db: Session = Depends(get_db)):
    db_quote = crud.get_random_quote(db)

    if db_quote is None:
        return {"message": "No quote available."}

    return db_quote


@app.get("/api/quotes/{quote_id}", response_model=schemas.Quote)
def read_quote(quote_id: int, db: Session = Depends(get_db)):
    db_quote = crud.get_quote(db, quote_id=quote_id)

    if db_quote is None:
        raise HTTPException(status_code=404, detail="Quote not found.")

    return db_quote


@app.get("/api/quotes/", response_model=list[schemas.Quote])
def read_quotes(db: Session = Depends(get_db)):
    quotes = crud.get_quotes(db)

    return quotes


@app.put("/api/quotes/{quote_id}", response_model=schemas.Quote)
def update_quote(
    quote_id: int, quote: schemas.QuoteCreate, db: Session = Depends(get_db)
):
    db_quote = crud.update_quote(db=db, quote_id=quote_id, quote=quote)

    if db_quote is None:
        raise HTTPException(status_code=404, detail="Quote not found.")

    return db_quote


@app.delete("/api/quotes/{quote_id}", response_model=schemas.Quote)
def delete_quote(quote_id: int, db: Session = Depends(get_db)):
    db_quote = crud.get_quote(db, quote_id=quote_id)

    if db_quote is None:
        raise HTTPException(status_code=404, detail="Quote not found.")

    crud.delete_quote(db, quote_id=quote_id)

    return db_quote

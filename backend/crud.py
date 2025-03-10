import random

from sqlalchemy.orm import Session

import models
import schemas


def get_quote(db: Session, quote_id: int):
    return db.query(models.Quote).filter(models.Quote.id == quote_id).first()


def get_quotes(db: Session):
    return db.query(models.Quote).all()


def create_quote(db: Session, quote: schemas.QuoteCreate):
    db_quote = models.Quote(**quote.dict())
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)

    return db_quote


def update_quote(db: Session, quote_id: int, quote: schemas.QuoteCreate):
    db_quote = db.query(models.Quote).filter(models.Quote.id == quote_id).first()

    if not db_quote:
        return None

    for key, value in quote.dict().items():
        setattr(db_quote, key, value)

    db.commit()
    db.refresh(db_quote)

    return db_quote


def delete_quote(db: Session, quote_id: int):
    db_quote = db.query(models.Quote).filter(models.Quote.id == quote_id).first()

    if db_quote:
        db.delete(db_quote)
        db.commit()

    return db_quote


def get_random_quote(db: Session):
    quotes = db.query(models.Quote).all()

    if not quotes:
        return None

    return random.choice(quotes)

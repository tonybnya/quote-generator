BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quote TEXT NOT NULL,
    author TEXT NOT NULL
);

INSERT INTO quotes (quote, author) VALUES
("The only limit to our realization of tomorrow is our doubts of today.", "Franklin D. Roosevelt"),
("The best way to predict the future is to invent it.", "Alan Kay"),
("Life is 10% what happens to us and 90% how we react to it.", "Charles R. Swindoll"),
("Your time is limited, so don't waste it living someone else's life.", "Steve Jobs"),
("The purpose of our lives is to be happy.", "Dalai Lama"),
("Get busy living or get busy dying.", "Stephen King"),
("You have within you right now, everything you need to deal with whatever the world can throw at you.", "Brian Tracy"),
("Believe you can and you're halfway there.", "Theodore Roosevelt"),
("The only way to do great work is to love what you do.", "Steve Jobs"),
("If you can dream it, you can do it.", "Walt Disney"),
("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
("Do not wait to strike till the iron is hot; but make it hot by striking.", "William Butler Yeats"),
("Success is not the key to happiness. Happiness is the key to success.", "Albert Schweitzer"),
("You miss 100% of the shots you don’t take.", "Wayne Gretzky"),
("I attribute my success to this: I never gave or took any excuse.", "Florence Nightingale"),
("The best revenge is massive success.", "Frank Sinatra"),
("The harder I work, the luckier I get.", "Gary Player"),
("Don’t watch the clock; do what it does. Keep going.", "Sam Levenson"),
("The secret of success is to do the common thing uncommonly well.", "John D. Rockefeller Jr."),
("You must be the change you wish to see in the world.", "Mahatma Gandhi"),
("Act as if what you do makes a difference. It does.", "William James"),
("Keep your face always toward the sunshine—and shadows will fall behind you.", "Walt Whitman"),
("The only place where success comes before work is in the dictionary.", "Vidal Sassoon"),
("What lies behind us and what lies before us are tiny matters compared to what lies within us.", "Ralph Waldo Emerson"),
("To succeed in life, you need two things: ignorance and confidence.", "Mark Twain"),
("It always seems impossible until it's done.", "Nelson Mandela"),
("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"),
("What you do today can improve all your tomorrows.", "Ralph Marston"),
("The only way to achieve the impossible is to believe it is possible.", "Charles Kingsleigh"),
("The biggest risk is not taking any risk.", "Mark Zuckerberg"),
("If God didn't exist, everything would be permissible.", "Dostoïevski");

COMMIT;

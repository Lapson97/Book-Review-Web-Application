import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

current_path = os.path.dirname(__file__)


def main():
    file = open(os.path.join(current_path, 'books.csv'), 'r')
    f = csv.reader(file)
    next(f)

    for isbn, title, author, year in f:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                {"isbn": isbn, "title": title, "author": author, "year": year})
        db.commit()
        print(f"Added book with ISBN: {isbn} Title: {title} Author: {author} Year: {year}")


if __name__ == '__main__':
    main()
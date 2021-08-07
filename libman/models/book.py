from libman import db
import random


class Book(db.Model):
    bookID = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    authors = db.Column(db.String(), nullable=False)
    average_rating = db.Column(db.Float(), nullable=False)
    isbn = db.Column(db.String(), nullable=False, unique=True)
    isbn13 = db.Column(db.String(), nullable=False, unique=True)
    language_code = db.Column(db.String(), nullable=False)
    num_pages = db.Column(db.Integer(), nullable=False)
    ratings_count = db.Column(db.Integer(), nullable=False)
    text_reviews_count = db.Column(db.Integer(), nullable=False)
    publication_date = db.Column(db.Date(), nullable=False)
    publisher = db.Column(db.String(), nullable=False)
    rent = db.Column(db.Integer(), nullable=False, default=random.randint(50, 100))
    memberID = db.Column(db.Integer(), db.ForeignKey("member.memberID"))

    def __init__(
        self,
        title,
        authors,
        average_rating,
        isbn,
        isbn13,
        language_code,
        num_pages,
        ratings_count,
        text_reviews_count,
        publication_date,
        publisher,
        rent,
    ) -> None:
        self.title = title
        self.authors = authors
        self.average_rating = average_rating
        self.isbn = isbn
        self.isbn13 = isbn13
        self.language_code = language_code
        self.num_pages = num_pages
        self.ratings_count = ratings_count
        self.text_reviews_count = text_reviews_count
        self.publication_date = publication_date
        self.publisher = publisher
        self.rent = rent

    def __repr__(self) -> str:
        return f"{self.title}"

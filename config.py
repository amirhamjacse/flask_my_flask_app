import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///site.db')  # SQLite as an example
    SQLALCHEMY_TRACK_MODIFICATIONS = False

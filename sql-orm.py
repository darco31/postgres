from sqlalchemy import (
    create_engine,Column,Float,ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine("postgres:///chinook")

base = declarative_base()
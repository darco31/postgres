from sqlalchemy import (
    create_engine, Column, Integer, String
)


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


#  Create a class based model for the programmer table.
class Games(base):
    __tablename__ = "Games"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre = Column(String)
    console = Column(String)
    age = Column(Integer, primary_key=False)
    

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)


# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


demon_souls = Games(
    name = "Demon Souls",
    genre = "Horror",
    console = "Playstation",
    age = 15,
)

final_fantasy = Games(
    name = "Final Fantasy",
    genre = "Sci-Fi",
    console = "Playstation",
    age = 12,
)


# add each instance of our programmers session
session.add(demon_souls)
session.add(final_fantasy)



# Commit our session to the database
session.commit()


# Query the database to find all programmers
game = session.query(Games)
for gamer in game:
    print(
        gamer.id,
        gamer.name,
        gamer.genre,
        gamer.console,
        gamer.age,
        sep=" | "
    )
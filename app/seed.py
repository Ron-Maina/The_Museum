from models import Museums, Artists, Artworks, museum_artist
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
import random

engine = create_engine('sqlite:///Museums.db')
session_maker = sessionmaker(bind=engine)
session = session_maker()

fake = Faker()

if __name__ == "__main__":
    # Clearing the database to avoid duplicate data
    print("CLEARING THE DATABASE*****")
    session.query(Museums).delete()
    session.query(Artists).delete()
    session.query(Artworks).delete()
    session.query(museum_artist).delete()
    print("DONE!")

    

    session.close()

    
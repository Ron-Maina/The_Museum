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
   
    
    
    artwork = [
    "Starry Night at the Alien Discotheque",
    "Mona Lisa's Mysterious Mona-lisa-tion",
    "The Persistence of Memory, Even During Monday Meetings",
    "The Scream (When You Run Out of Coffee)",
    "Guernica: Picasso's Cubist Pizza Party",
    "The Last Supper (When They Ran Out of Bread)",
    "The Birth of Venus (Mermaid Edition)",
    "The Starry Night (Van Gogh's Starry Starbucks)",
    "American Gothic (Farmers with Fancy Forks)",
    "Water Lilies: Monet's Puddle Collection",
    "The Kiss (When You Accidentally Kiss the Wrong Person)",
    "The Girl with a Pearl Earring (and Sunglasses)",
    "The Persistence of Memory (Einstein's Forgotten Alarm Clock)",
    "The Great Wave off Kanagawa (Surfing on Sushi)",
    "Whistler's Mother (Whistling While Knitting)",
    "The Night Watch (Stalking the Midnight Snackers)",
    "The Garden of Earthly Delights (Weed Control Nightmare)",
    "The School of Athens (Where Plato and Aristotle Cut Class)",
    "The Birth of Adam (When God Gave Adam an iPhone)",
    "The Death of Sardanapalus (Sardanapalus' Failed Cooking Show)",
    "Nighthawks (Owls in a Late-Night Diner)",
    "The Sleeping Gypsy (Gypsy Taking a Cat Nap)",
    "The Elephants (When Elephants Tried to Play Chess)",
    "The Son of Man (Surrealist Apple Head)",
    "The Dance (Dancing with Dinosaurs)",
    "The Red Studio (Van Gogh's Paint Spill Disaster)",
    "No. 5, 1948 (Abstract Paint Can Explosion)",
    "The Arnolfini Portrait (Couple with a Selfie Stick)",
    "Composition VIII (Abstract Art Class Fail)",
    "Luncheon on the Grass (Picnic with Plush Toys)",
    "Les Demoiselles d'Avignon (Avignon's Wild Girls Night Out)",
    "The Girl before a Mirror (When the Mirror Talks Back)",
    "The Persistence of Memory (Lost in a Salvador Dali Dream)",
    "The Weeping Woman (When You Can't Find Your Keys)",
    "The Bedroom (Van Gogh's IKEA Shopping List)",
    "The Persistence of Memory (Clocks on Vacation)",
    "The Dream (When You Dream of Pizza)",
    "The Basket of Apples (An Apple a Day Keeps the Doctor Away)",
    "The Treachery of Images (This is Not a Painting, Seriously)",
    "The Thinker (Thinking About What to Order for Dinner)",
    ]

    for artist in artists_list:
        for art_name in artwork:
            art = Artworks(
                name= art_name,
                year_made= fake.date(),
                year_added_to_museum= fake.date(),
                museum_id= random.randint(1,5),
                artist_id= artist.id
            )
        session.add(art)
        session.commit()

    
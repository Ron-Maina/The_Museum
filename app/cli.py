#!/usr/bin/env python3
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Museums, Artists, Artworks, museum_artist
import click
import sys

engine = create_engine('sqlite:///Museums.db')
session_maker = sessionmaker(bind=engine)
session = session_maker()

# Enter Code Here
elif choice == 2:
            def menu_2():
                click.echo("\nAre you: ")
                for i, selection in enumerate(["New Artist", "Existing Artist"], 1):
                    click.echo(f"{i}. {selection}")
                append(menu_2)
            menu_2()
            
            selected = click.prompt("\nSelect: ")
            def new_artwork():
                art_name = click.prompt("\nEnter Artwork Name: ")
                date_of_artwork = click.prompt("\nEnter Date of Artwork: ")
                date_of_exhibition = click.prompt("\nEnter Exhibition Date: ")

                new_artwork = Artworks(
                    name = art_name,
                    date_of_artwork = date_of_artwork,
                    date_of_exhibition = date_of_exhibition,
                    museum_id = museum_choice,
                    artist_id = existing_artist.id
                )
                session.add(new_artwork)
                session.commit()


            existing_artist = session.query(Artists).order_by(Artists.id.desc()).first()
            if selected == "1":
                def new_artists():
                    rating = click.prompt("\nEnter your rating: ", type=int)
                    if rating < 3:
                        click.echo("CANNOT BE APPROVED! RATING MUST BE HIGHER THAN 3!")
                        display_museums()

                    elif 3 <= rating <= 5:
                        first_name = click.prompt("\nEnter your first name: ")
                        last_name = click.prompt("\nEnter your last name: ")
                        
                        new_artist = Artists(
                            first_name = first_name,
                            last_name = last_name,
                            rating = rating
                        )
                        session.add(new_artist)
                        session.commit()

                        new_artwork()
                        
                        new_data = session.query(Artworks).order_by(Artworks.id.desc()).first()
                        data = museum_artist.insert().values(museum_id = new_data.museum_id, artists_id = new_data.artist_id)
                        session.execute(data)
                        session.commit()
                        click.echo("APPROVED!")
                    append(new_artists)
                new_artists()
            
            elif selected == "2":
                def update_artist():
                    first_name = click.prompt("\nEnter your first name: ")
                    last_name = click.prompt("\nEnter your last name: ")

                    existing_artist = session.query(Artists).filter_by(first_name = first_name, last_name = last_name).first()
                    if existing_artist == None:
                        click.echo("USER NOT FOUND")
                    else:
                        new_artwork()
                        click.echo("APPROVED!")
                    append(update_artist)
                update_artist()

            else:
                click.echo("INVALID INPUT")

        final = click.prompt("\nType (q) to exit")
        if final == "q":
            click.echo("Exiting the Program!") 
            sys.exit()
        
        else:
            click.echo("INVALID INPUT")

        


                    


if __name__ == '__main__':
    cli()
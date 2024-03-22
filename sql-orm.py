from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-base model for the "artist" table
class Artist(base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String,)

# create a class-base model for the "album" table
class Album(base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("artist.artist_id"))

# create a class-base model for the "track" table
class track(base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer,ForeignKey("album.album_id"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of a sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens and actual session by calling Session() subclass defined above
session = Session()


# creating the database using declarative_base subclass
base.metadata.create_all(db)


# Query1 - select all records from the "artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.artist_id, artist.name, sep=" | ")

# Query2 - select only the "name" column from the "artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.name)

# Query3 - select only "Queen" from the "artist" table
# artist = session.query(Artist).filter_by(name = "Queen").first()
# print(artist.artist_id, artist.name, sep=" | ")

# Query4 - select only by "artist_id" #51 from the "artist" table
# artist = session.query(Artist).filter_by(artist_id=51).first()
# print(artist.artist_id, artist.name, sep=" | ")

# Query5 - select only the albums with the "artist_id" #51 in the "album" table
albums = session.query(Album).filter_by(artist_id=51)
for album in albums:
    print(album.album_id, album.title, album.artist_id, sep=" | " )

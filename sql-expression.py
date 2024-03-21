from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData 
) 

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "artist" table
artist_table = Table(
    "artist", meta,
    Column("artist_id", Integer, primary_key=True),
    Column("name", String)
)

# create a variable for "album" Table
album_table = Table(
    "album", meta,
    Column("album_id", Integer, primary_key=True),
    Column("title", String),
    Column("artist_id", Integer, ForeignKey("artist_table.artist_id"))
)

# create a variable for "Track" table
track_table = Table(
    "track", meta,
    Column("track_id", Integer, primary_key=True),
    Column("name", String),
    Column("album_id", Integer, ForeignKey("album_table.album_id")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:

    # Query1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query2 - select only the "name" column from the "artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.name])

    # Query3 - select only 'Queen' from the "artist" table
    # select_query = artist_table.select().where(artist_table.c.name =="Queen")

    # Query4 - select only by "artist_id" #51 from the "artist" table
    # select_query = artist_table.select().where(artist_table.c.artist_id == 51)

    # Query5 - select only the albums with "artist_id" #51 from the "album" table
    # select_query = album_table.select().where(album_table.c.artist_id== 51)


    results = connection.execute(select_query)
    for result in results:
        print(result)
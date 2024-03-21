from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Interger, String, MetaData 
) 

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "artist" table
artist_table = Table(
    "Artist", meta,
    Column("Artist_id", Interger, primary_key=True),
    Column("Name", String)
)

# create a variable for "album" Table
album_table = Table(
    "album", meta,
    Column("AlbumnId", Interger, primary_key=True),
    Column("Title", String),
    Column("Artist_Id", Interger, ForeignKey("artist_table.Artist_Id"))
)

# create a variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("Track_Id", Interger, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Interger, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Interger, primary_key=False),
    Column("GenreId", Interger, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Interger),
    Column("Bytes", Interger),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:

    # Query1 - select all records from the "Artist" table
    select_query = artist_table.select()

    results = connection.execute(select_query)
    for result in results:
        print(result)
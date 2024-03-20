import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# create a cursor object of the database
cursor = connection.cursor()

# Query1 - select all items from the "Artist" table
# cursor.execute('SELECT * FROM "artist"')

# Query2 - select only the "name" column from the "artist" table
# cursor.execute('SELECT "name" FROM "artist"')

# Query3 - select only "Queen" from the "artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"] )

# Query 4 - select only by "artist_id" #51 from the "artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s', [51] )

# Query5 - select only the albums with the "artist_id" #51 on the "album" table
# cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51] )

# Queey 6 - select all tracks where the composer is "Queen" from the "track" table
cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"] )

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
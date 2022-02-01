from db.run_sql import run_sql
from models.artist import Artist


# List All Artists
def select_all():
    artists =[]

    sql = "SELECT * FROM artists"
    result = run_sql(sql)

    for row in result:
        artist = Artist(row['name'], row['id'] )
        artists.append(artist)
    return artists

# Delete all Artists
def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)


# Create and Save Artist
def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    result = run_sql(sql, values)
    id = result[0]['id']
    artist.id = id
    return artist

# Find Artists by their ID (select)
def select_by_id(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        artist = Artist(result['name'], result['id'])
    return artist
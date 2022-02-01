from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repo

# Create and Save Album
def save(album):
    
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING id"
    values = [album.title, album.genre, album.artist.id]
    result = run_sql(sql, values)
    id = result[0]['id']
    album.id = id
    return album

# List All Albums
def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for result in results:
        artist = artist_repo.select_by_id(result['artist_id'])
        album = Album(result['title'], result['genre'], artist, result['id'])
        albums.append(album)

    return albums

# Find Album by their ID
def select_by_id(id):
    album = None

    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        album = Album(result['title'], result['genre'], result['artist_id'], result['id'])

    return album

# Delete all Albums
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)




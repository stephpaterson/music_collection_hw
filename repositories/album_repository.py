from db.run_sql import run_sql
from models.album import Album

# Create and Save Album
def save(album):
    sql = "INSERT INTO albums (title, genre) VALUES (%s, %s) RETURNING id"
    values = [album.title, album.genre]
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
        album = Album(result['title'], result['genre'], result['id'])
        albums.append(album)

    return albums

# Find Album by their ID
def select_by_id(id):
    album = None

    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        album = Album(result['title'], result['genre'], result['id'])

    return album

# Delete all Albums
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)




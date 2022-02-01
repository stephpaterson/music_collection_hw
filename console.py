import pdb

from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repo
import repositories.artist_repository as artist_repo

artist_repo.delete_all()

artist = Artist("Fat Boy Slim")
artist_repo.save(artist)

album = Album("You've come a long way, baby", "Electronic")
album_repo.save(album)

list_artists = artist_repo.select_all()
list_albums = album_repo.select_all()

pdb.set_trace()
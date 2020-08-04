import pdb

from models.album import Album
from models.artist import Artist

import repo.album_repo as album_repo
import repo.artist_repo as artist_repo

album_repo.delete_all()
artist_repo.delete_all()

artist_1 = Artist("Jack White")
artist_repo.save(artist_1)

artist_2 = Artist("Ben Howard")
artist_repo.save(artist_2)

album_1 = Album("Seven Nation Army", "Indie",artist_1)
album_repo.save(album_1)

album_2 = Album("Every Kingdom", "Indie",artist_2)
album_repo.save(album_2)

album_3 = Album("I forget where we were", "Indie", artist_2)
album_repo.save(album_3)

# artists = artist_repo.select_all()
# print(artists)

found_album = album_repo.select(album_2.id)
print(found_album.artist.name)

pdb.set_trace()
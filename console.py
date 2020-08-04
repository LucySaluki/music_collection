import pdb

from models.album import Album
from models.artist import Artist

import repo.album_repo as album_repo
import repo.artist_repo as artist_repo

artist_repo.delete_all()

artist_1 = Artist("Jack White")
artist_repo.save(artist_1)

artist_2 = Artist("Ben Howard")
artist_repo.save(artist_2)

album_1 = Album("Seven Nation Army", "Indie",artist_1)
album_repo.save(album_1)

pdb.set_trace()
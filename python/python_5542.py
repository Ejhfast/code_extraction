# help with datastore query
songs = GqlQuery('SELECT __key__ FROM song WHERE artist = :1', 'john-lennon')
playlists = GqlQuery('SELECT * FROM playlist WHERE songs IN :1', songs)

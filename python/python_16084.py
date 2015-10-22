# Getting a tracklist from MusicBrainz
result = musicbrainzngs.get_releases_by_discid(disc.id, includes=["artists", "recordings"])

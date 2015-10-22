# How to set multiple validators to a field in web2py?
db.aetitles.hospital_id.requires = [IS_NOT_EMPTY(),
                                IS_IN_DB(db, db.hospitals.id, '%(title)s')]

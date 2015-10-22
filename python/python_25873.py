# Check class creation in OrientDB
SELECT FROM ( SELECT expand( classes ) FROM metadata:schema ) WHERE name = 'OUser'

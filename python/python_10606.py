# Facebook Python SDK - Upload image in Event Create
graph = facebook.GraphAPI(oauth_access_token)
tags = json.dumps([{'x':50, 'y':50, tag_uid:12345}, {'x':10, 'y':60, tag_text:'a turtle'}])
graph.put_photo(open('img.jpg'), 'Look at this cool photo!', album_id_or_None, tags=tags)

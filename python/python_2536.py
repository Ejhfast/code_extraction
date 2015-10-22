# Fetching just the Key/id from a ReferenceProperty in App Engine
story = db.get(story_key)
author_id = Story.author.get_value_for_datastore(story).id()

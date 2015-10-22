# App engine Python NDB map_async using callback, objects and inheritance pattern
query = Docs.query()
multi_future = query.map_async(lambda entity: P(...).callback(entity))

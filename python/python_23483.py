# GAE python ndb - How to get_by_id with projection?
Content.query(Content.key == ndb.Key('Content', content_id)).get(projection=['etag'])

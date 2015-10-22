# How to query for empty records in many to many relation
session.query(BlogPost).filter(BlogPost.authors.any())

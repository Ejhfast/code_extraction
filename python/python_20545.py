# Peewee ORM get similar entries based on foreign key
# Articles tagged with 'tag1'
Articles.select().join(ArticleTags).join(Tags).where(Tags.name == 'tag1')

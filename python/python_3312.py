# What type is on the other end of relation in sqlalchemy without creating objects?
for prop in class_mapper(Shelf).iterate_properties:
    if isinstance(prop, sqlalchemy.orm.RelationshipProperty):
       print prop.mapper.class_

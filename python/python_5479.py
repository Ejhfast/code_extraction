# sqlalchemy: referencing label()'d column in a filter or clauselement
t = DBSession.query(Tag.tid.distinct().label('tid')).subquery('t')
test = select([bmarks_tags.c.bmark_id], bmarks_tags.c.tag_id == t.c.tid)
return DBSession.execute(test)

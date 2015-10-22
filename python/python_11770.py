# how to cleanly remove ndb properties
if 'propname' in ent._properties:
  del ent._properties['propname']
  ent.put()

# Google App Engine and Django templates: why do these two cases differ?
entries = db.Query(Entry).order("-published").fetch()
comments = db.Query(Comment).order("published").fetch()

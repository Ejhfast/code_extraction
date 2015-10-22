# How can I make my App Engine Datastore user search faster?
db.GqlQuery("SELECT * FROM User WHERE email &gt;= :1 AND email &lt;= :2", searchData, unicode(searchData) + u"\ufffd")

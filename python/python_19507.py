# Delete entities having datetime older than N seconds from google-app-engine ndb
import datetime
earliest = datetime.datetime.now() - datetime.timedelta(days=7)
Mjcode.query(Mjcode.date &lt;= earliest).fetch(keys_only=True)

# How can i grab the domain name from the firefox's places.sqlite file with python script
import sqlite3
db = sqlite3.connect("&lt;path_to&gt;/places.sqlite")
urls = db.execute("select url from moz_places").fetchall()

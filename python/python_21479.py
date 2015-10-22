# How would I clear all data in a selected column in a created SQL database?
con.cursor().execute("UPDATE Users SET Username = NULL")

# designing a database in google app engine
user = db.GqlQuery("SELECT * FROM Users WHERE login IS :1", login)

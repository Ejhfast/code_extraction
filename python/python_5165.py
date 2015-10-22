# gql query returns BadQueryError: Parse Error
data = db.GqlQuery("SELECT * FROM Playlist WHERE tags = :1 ORDER BY :2", tag, order)

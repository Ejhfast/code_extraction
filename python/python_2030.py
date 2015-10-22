# GQL how to select by UserProperty
query = GqlQuery("SELECT * FROM Atable WHERE owner = :1", users.get_current_user())

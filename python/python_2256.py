# How do I check for Existence of a Record in GAE
profile = db.GqlQuery("SELECT * FROM Profile WHERE account = :1",
                        users.get_current_user()).get()

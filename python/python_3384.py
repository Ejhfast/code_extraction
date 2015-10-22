# How to make a light query for a many to many relationship in Google Apps Engine?
list_keys = [ListUser.list.get_value_for_datastore(list_user)
              for list_user in list_users]
lists = db.get(list_keys)

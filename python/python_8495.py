# Boolean value inconsistent
theuser = UserTable.get_by_key_name(Theusername)
theuser.isVerified = True
theuser.put()

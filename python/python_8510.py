# When I try a syncdb, where is the duplicate user_id error coming from?
post_save.connect(create_user_profile, sender = User, dispatch_uid="create_user_profile")

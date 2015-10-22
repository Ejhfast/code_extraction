# User signup leads to IntegrityError
post_save.connect(create_user_profile, sender=User,
                    dispatch_uid="user_create_profile")

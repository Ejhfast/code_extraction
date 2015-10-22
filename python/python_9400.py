# Extending user model form with custom fields
user_profile = new_user.get_profile()
user_profile.company = company
user_profile.save()

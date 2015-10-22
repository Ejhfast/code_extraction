# Find each user object for list of user ids
following_users_list_data = User.query.filter(User.id.in_(following_users)).all()

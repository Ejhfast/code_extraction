# Joining two lists that correspond to each other to create a list of class objects
users = [User(user, password) for user, password in zip(usernameList, passwordList)]

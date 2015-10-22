# NDB projection of instance Key or ID
return Users.query(Users.user_email == email).get(projection=[Users.password])

# update multiples fields with sql alchemy
data = { "email" : "my_new_email@example.com", "age" : 20, "city" : "London", "country" : "UK", "language" : "English", "profession" : "developer", "employeer" : "BBC" }
User.query.filter_by(username='admin').update(data)
db.session.commit()

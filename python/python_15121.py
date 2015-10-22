# How to pass an array of conditions in mongokit find query
conditions = {'title':{'$regex':'test'},'status':{'$regex':'active'} ..... other conditions }
data = db.entry.find(conditions).limit(3);

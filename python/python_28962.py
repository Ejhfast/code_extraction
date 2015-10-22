# OR condition in motor python
doc = yield db.student.find_one({ "$or": [{"academy": name}, {"sports": name}]})

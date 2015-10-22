# Pymongo, query on list field, and/or
yourmongocoll.find({"vals":1100})
yourmongocoll.find({"$or":[ {"vals":1700}, {"vals":100}]})
yourmongocoll.find({"$and":[ {"vals":100}, {"vals":1100}]})

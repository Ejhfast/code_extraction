# How to delete pymongo.Database.Database object
client = MongoClient(host=MONGO_HOST,port=27017,max_pool_size=200)
client.drop_database("database_name")

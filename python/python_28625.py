# Start a scrapy spider TypeError: object.__new__(thread.lock) is not safe, use thread.lock.__new__()
import pymongo
client = pymongo.MongoClient(DB_URL)

# How to increase connection pool size for Mongodb using python
from pymongo import MongoClient
client = MongoClient('host', port, maxPoolSize=200)

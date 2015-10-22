# How to get health of an elasticsearch cluster using python API?
from elasticsearch import Elasticsearch
es = Elasticsearch()
print(es.cluster.health())

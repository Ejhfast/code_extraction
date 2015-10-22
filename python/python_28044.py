# How to update a document using elasticsearch-py?
coll = Elasticsearch()
coll.update(index='stories-test',doc_type='news',id=hit.meta.id,
                body={"doc": {"stanford": 1, "parsed_sents": parsed }})

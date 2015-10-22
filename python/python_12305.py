# Python - How to select ObjectId
lowest_id = min(items, key=lambda i: i['score'])['_id']

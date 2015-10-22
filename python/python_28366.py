# lambda for RDD query with if statement
badRecords = access_logs.filter(lambda log: log.response_code == 404)

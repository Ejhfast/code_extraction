# HTTP 500 error on Streaming insert Python
response = self.tabledata.insertAll(projectId=PROJECT_ID, datasetId='hunter', tableId='test', body={rows: [{json: {userid: 1, client: 1, type: 1, time: 0.0}}, ...]}).execute()

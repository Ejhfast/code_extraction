# Error message: The format indicated had no available deserialization method
r=requests.post(url='http://localhost:8000/api/open/',
                data=json.dumps({"name":"awdawd"}),
                headers={'content-type':'application/json'})

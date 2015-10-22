# django/python How to connect to a webservice by posting a json
payload = {'key1': 'value1', 'key2': 'value2'}
&gt;&gt;&gt; r = requests.post("http://www.example.com/webservice", data=payload)
&gt;&gt;&gt; print r.text

# Create CKAN dataset using CKAN API and Python Requests library
head['Content-Type'] = 'application/x-www-form-urlencoded'
in_dict = urllib.quote(json.dumps(in_dict))
r = requests.post(url, data=in_dict, headers=head)

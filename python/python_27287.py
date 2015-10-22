# Python requests library - Strange behavior vs curl
response = requests.get('http://localhost:81/proxy/bparc/my_key')
print len(response.content)

# Django rejects Requests' CSRF Token
cookies = dict(client.cookies)
r = requests.post(URL+"au", data=json.dumps(data), headers=headers,cookies=cookies)

# python-oauth2 with Twitter's oauth_callback
resp, content = client.request(request_token_url, "POST",body=urllib.urlencode({'oauth_callback':my_callback_url}))

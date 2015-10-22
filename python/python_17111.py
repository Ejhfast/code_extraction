# Pep8 E501: line too long error
header, response = client.request(
   'https://api.twitter.com/1.1/statuses/user_timeline.'
   'json?include_entities=true&amp;screen_name=' + username + '&amp;count=1')

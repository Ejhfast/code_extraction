# Given a big list of urls, what is a way to check which are active/inactive?
requests.head('http://httpbin.org/get').status_code

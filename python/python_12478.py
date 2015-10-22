# How to export a cookie in a file to use with python scrapy
request_with_cookies = Request(url="http://www.example.com",
                           cookies={'currency': 'USD', 'country': 'UY'})

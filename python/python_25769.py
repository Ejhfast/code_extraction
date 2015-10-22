# How to capture python SSL(HTTPS) connection through fiddler2
requests.get("https://www.python.org", proxies={"http": "http://127.0.0.1:8888", "https":"http:127.0.0.1:8888"},verify=r"FiddlerRoot.pem")

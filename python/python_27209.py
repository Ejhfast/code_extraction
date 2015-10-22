# Requests does not return html anymore - Python
html = requests.get(url, headers={"User-Agent": "Requests"}).content

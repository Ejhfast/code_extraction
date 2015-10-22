# Scraping Metacritic with urllib to follow redirect
response = requests.get(url)
newUrl = response.url

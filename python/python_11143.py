# python 3, errorhandling urllib requests
except urllib.error.URLError as e: ResponseData = e.read().decode("utf8", 'ignore')

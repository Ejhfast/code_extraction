# How to parse the hashed arguments (with # instead of ?) in url in GAE with python?
import urlparse
access_token = urlparse.parse_qs(urlparse.urlsplit(url).fragment).get('access_token')

# How to get a Url segment in django
import urlparse
path = urlparse.urlsplit(uri).path
print path.split('/')[n]

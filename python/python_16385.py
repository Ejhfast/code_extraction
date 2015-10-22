# how to run following python code in google app engine backend
from google.appengine.ext import deferred
deferred.defer(yourfile.your_fetcher_method, _target='mybackend')

# using unicode in Google translate url from python script
url = 'https://ajax.googleapis.com/ajax/services/language/translate?v=1.0&amp;q=' \
    + urllib2.quote(mytext) + '&amp;langpair=ru%7Cen'

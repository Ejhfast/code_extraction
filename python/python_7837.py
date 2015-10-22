# Xpath query to get the parent Element text and its child element attribute values?
string-join(/sample//Message[@number = 2]/Description/(text() | */@*), '')

# Problem passing XML to HTTP Post api using urllib in Python
xml_string = "&lt;list&gt;&lt;FilterItems&gt;&lt;FilterItem attribute='pageNumber' value='1'/&gt;&lt;/FilterItems&gt;&lt;/list&gt;"
 data = (xml_string)
 req = urllib2.Request(url,data)

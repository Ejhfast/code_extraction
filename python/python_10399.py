# Displaying results from search API
address = "http://www.blekko.com/?q='%(query)s'+/html&amp;auth=&lt;mykey&gt;" % dict(query=request.vars.query)

# how to return a dictionary in python django and view it in javascript?
import json
data = {'val1' : 'this is x', 'val2' : True}
return HttpResponse( json.dumps( data ) )

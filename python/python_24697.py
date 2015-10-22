# Get post data from ajax post request in python file
def index(req):
        postData = req.form
        json = str(postData['param'].value)

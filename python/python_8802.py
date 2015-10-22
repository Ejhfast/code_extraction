# How do I redirect an user back to the page they were trying to access once they log in? (Django)
response = HttpResponseRedirect(next)
# Do whatever else you need to do here with the response object
return response

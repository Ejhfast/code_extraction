# HTTP POST, curl and mod_python - How to handle POST request without HTML FORM element?
def path(req):
    request_data = req.form.getfirst('request')

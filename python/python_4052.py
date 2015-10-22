# web2py redirect to previous page
if request.env.http_referer:
    redirect(request.env.http_referer)

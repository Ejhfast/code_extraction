# Return a requests.Response object from Flask
return (resp.text, resp.status_code, resp.headers.items())

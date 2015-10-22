# How to delete a user's cookie using python on app engine?
self.response.headers.add_header("Set-Cookie", "access_token=deleted; Expires=Thu, 01-Jan-1970 00:00:00 GMT")

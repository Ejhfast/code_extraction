# Python facebook-sdk post to page
graph = facebook.GraphAPI(page_access_token)
graph.put_object("page id", "feed", message='My message goes here')

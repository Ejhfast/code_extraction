# Send HTTP response that doesn't change the user's current page
@app.route('/')
def index():
    return flask.Response("Foo bar baz"), 204

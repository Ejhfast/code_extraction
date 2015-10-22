# How to write in flask a function that is able to treat arbitrary requests?
@app.route("/&lt;path&gt;")
def default(path=None):
    return path

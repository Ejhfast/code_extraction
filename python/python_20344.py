# How to get name of a required page in flask?
@app.route("/hello&lt;path:path&gt;.py")
def hello(path):
    return "Hello World!"

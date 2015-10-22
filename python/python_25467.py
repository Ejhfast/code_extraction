# href attribute value not working in Python Flask app for target HTML pages
@app.route('/index.html')
def index():
    return render_template('index.html')

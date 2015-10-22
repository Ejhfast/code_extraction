# Download file from local folder
@app.route('/process/&lt;user_id&gt;/&lt;file_format&gt;/&lt;download&gt;')
def download(user_id, file_format, download):
    return redirect(url_for('static', filename='documents/'+download))

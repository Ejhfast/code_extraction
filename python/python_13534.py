# Flask WTF form not updating with the sqlite3 database
form = DatabaseForm()
    form.images.choices = [(str(x[0]), x) for x in listOfRows]
    if form.validate_on_submit():

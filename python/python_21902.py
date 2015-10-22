# How do you update multiple values in flask-sqlalchemey?
query.update({'home_score': request.form['home_score'],
              'away_score': request.form['away_score']})

# How to test redirect to created instance in Flask
...
q = Question.query.filter_by(title='What about somestuff in Flask?').first()
self.assertRedirects(response, '/questions/%d/' % q.id)

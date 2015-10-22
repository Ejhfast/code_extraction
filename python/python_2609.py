# How to save user's daily progress?
class DailyProgress(db.Model):
    date = db.DateTimeProperty(auto_now_add=True)
    score = db.IntegerProperty()

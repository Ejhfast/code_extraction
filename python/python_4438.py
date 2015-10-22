# How to "run" a "Paypal Subscriptions Service" inside Google App Engine?
class Users(db.Model):
  gae_user_object = db.UserProperty()
  premium_member = db.BooleanProperty(default=False)

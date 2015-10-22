# How can i set email_token_expiry time for 24 hours?
import datetime
obj.email_token_expiry = datetime.datetime.now()+datetime.timedelta(hours=24)

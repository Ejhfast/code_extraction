# Datetime field on Django to store the date of insertion of row?
date_inserted    = models.DateTimeField(auto_now_add=True)
date_last_update = models.DateTimeField(auto_now=True)

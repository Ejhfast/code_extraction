# Order django-tables2 by name instead of FK
Owner = tables.Column(order_by=("Owner.Full_Name"))

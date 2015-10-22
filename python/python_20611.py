# Why won't Django Model's time field default properly to utcnow() as expected?
timeStamp = models.DateTimeField(default=datetime.datetime.utcnow)

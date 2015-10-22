# Filter ForeignKey by Boolean value in django
client = models.ForeignKey(Client, limit_choices_to = {'is_provider': True})

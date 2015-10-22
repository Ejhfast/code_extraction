# Django models -Best way to store multiple contact numbers
contact_info = ArrayField(models.CharField(max_length=15), blank=True)

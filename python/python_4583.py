# Set today date as default value in the model
vote_date = models.DateField(_('vote date'), null=False, blank=False, auto_now=True)

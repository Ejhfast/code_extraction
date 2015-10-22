# Trying to query for all objects with a foreign key reference to an entry with a certain value in one of its fields
first_warning_list = ListWarning.objects.filter(mailing_list__name='PH_212', first_warning=True, last_warning=False)

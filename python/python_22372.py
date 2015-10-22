# Django : Limit records in database based on foreign key
def clean(self):
    if MyTable.objects.filter(user=self.user).count()&gt;=2:
        raise ValidationError('Only 2 entries per user allowed')

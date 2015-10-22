# Sort by field in ForeignKey model
class Meta:
    ordering = ['user__first_name', 'user__last_name']

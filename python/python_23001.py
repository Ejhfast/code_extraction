# Django: When saving input from drop down lists, saves option value instead of actual value
teams = forms.ModelChoiceField(queryset= All_teams.objects.all().order_by('team_name'), to_field_name="team_name")

# DJANGO: blank select option missing in form
manager = forms.CharField(required=False, widget=Select(choices=(('', '----------'),) + LIST), label='Their Position?')

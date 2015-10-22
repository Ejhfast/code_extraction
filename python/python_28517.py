# Read a variable that is placed inside my models file, in another file
type = forms.CharField(label='Type', widget=forms.Select(choices=User.USER_TYPE_CHOICES))

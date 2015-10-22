# Is there a way in Django to make it so that when a form with initial text is clicked the text disappears?
Username =forms.CharField(max_length=35,
                          required=True,
                          widget=forms.TextInput(attrs={'placeholder': 'Username'}))

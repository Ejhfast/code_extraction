# how to add multiple attrs in Django forms
email = forms.EmailField(
    widget = forms.TextInput(attrs={'placeholder': 'Email', 'class': 'myClass', 'size': 'mySize'}))

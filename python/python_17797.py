# django form fields are not showing up in template - why?
class AddBook(forms.Form):
    titel = forms.CharField(widget=forms.TextInput())
    author = forms.CharField(widget=forms.TextInput())

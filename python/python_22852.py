# Django dealing with bootstrap form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput().attrs={'class': 'form-control','placeholder':'Usuario' })
    password=forms.CharField(max_length=30,widget=forms.PasswordInput().attrs={'class': 'form-control','placeholder':'Password' })

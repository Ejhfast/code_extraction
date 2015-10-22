# Custom django user registration form
class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')

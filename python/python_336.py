# Django form - set label
def __init__(self, *args, **kwargs):
    super(RegistrationFormTOS, self).__init__(*args, **kwargs)
    self.fields['email'].label = "New Email Label"

# Django how to override form validation for a required field
def __init__(self, *args, **kwargs):
    super(MyForm, self,).__init__(*args, **kwargs)
    self.fields['password'].required = False

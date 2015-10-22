# Cache problem with Django forms
def __init__(self, *args, **kwargs):
   super(MyForm, self).__init__(*args, **kwargs)
   self.fields['year'].choices = self.get_years()

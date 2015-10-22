# django: Changing auto_id of ModelForm based form class
class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(auto_id=True, *args, **kwargs)

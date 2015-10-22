# Django model: creating small value fixed point
class MyModuleForm(forms.Form):
    ....
    pseudoDecimalField = forms.PositiveSmallIntegerField(widget=forms.TextInput)

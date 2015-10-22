# How Can I attach multiple forms to a single submit button in Django?
class DocumentForm(forms.Form):
    form1 = forms.FileField()
    form2 = forms.FileField()

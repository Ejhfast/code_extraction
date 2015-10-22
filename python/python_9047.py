# Django forms.py not getting updated with new values from DB
class Test2(forms.ModelForm):
    templates = forms.ModelChoiceField(queryset=Test.objects.filter(template=True))

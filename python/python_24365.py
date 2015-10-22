# How do I 'check' a radio button value using django RadioSelect widget
class ServiceForm(forms.ModelForm):
    regular_service = forms.ChoiceField(required = True, choices = CHOICES, widget=forms.RadioSelect(attrs={'class' : 'Radio'}), initial=1)

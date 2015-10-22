# Django - ModelChoiceField - TypeError - __init__() takes at least 2 arguments (1 given)
class QueueForm(forms.Form):
queue = forms.ModelChoiceField(queryset=Order.objects.all())

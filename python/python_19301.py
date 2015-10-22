# Get List of objects in django form
company = forms.ModelChoiceField(queryset=Company.objects.all(), required=False, help_text="Company")

# django dropdownlist onchange submission
days = forms.ModelChoiceField(queryset=Day.objects.all().order_by('alias'), widget=forms.Select(attrs={"onChange":'refresh()'}))

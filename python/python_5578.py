# Django forms, getting a select box from a different model
category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                  empty_label="(Nothing)")

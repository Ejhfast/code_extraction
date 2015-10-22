# Convert CharField to ChoiceField Dynamically in Django Forms?
choices = (('sample', Sample'), ('testing 'Testing'))
self.fields['duration']  = forms.ChoiceField(choices=choices, label="Duration")

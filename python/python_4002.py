# In Django, how do i change "This field is required." to "Name is required"?
name = forms.CharField(error_messages={'required': 'Your Name is Required'})

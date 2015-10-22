# Django: Optional model form field
questions = forms.CharField(help_text="Do you have any questions?", widget=forms.Textarea, required=False)
about_yourself = forms.CharField(help_text="Tell us about yourself", widget=forms.Textarea, required=False)

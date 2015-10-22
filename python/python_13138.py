# Add extra parameter to inlineformset_factory
def set_extra_forms(extra_forms, **kwargs):
    EmploymentFormSet = inlineformset_factory(Profile, Employment, form=EmploymentForm, extra=extra_forms)
    return EmploymentFormSet(**kwargs)

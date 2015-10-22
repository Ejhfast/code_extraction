# Can a ModelForm accept __init__ parameters when used in a Formset?
formset.form.base_fields['exp_pocket'].queryset = Pockets.objects.filter(pocket_owner=request.user)

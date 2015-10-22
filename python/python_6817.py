# Django form object has no attribute issue
if not picture.objects.filter(id=form.cleaned_data['ordered_picture']).exists():

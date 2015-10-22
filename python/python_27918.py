# Model formset refresh extra field disappears
if formset.is_valid():
    formset.save()
    return HttpResponseRedirect('/')

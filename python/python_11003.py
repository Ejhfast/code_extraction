# Django form submission not refreshing what user sees
if formset.is_valid():
    formset.save()
    return HttpResponseRedirect("")

# Why doesn't a formset provide values like a form in Django?
IPTCFormSet = modelformset_factory(IPTCForm)
formset = IPTCFormSet(queryset=IPTC.objects.all())

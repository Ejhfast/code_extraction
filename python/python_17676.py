# Django FormWizard Filtering ChoiceField
consummer = ServicesActivated.objects.filter(status=1)
consummer = consummer.exclude(name__exact=data['provider'])
form = ConsummerForm(instance=consummer)

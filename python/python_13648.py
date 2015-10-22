# Django inline formsets and choicefields generate too many db queries
field_queryset = Test.objects.all()
for form in formset:
        form.fields['test_field'].queryset = field_queryset

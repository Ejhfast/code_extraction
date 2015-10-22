# Django query sets on many-2-many field
self.fields['business'].queryset = Business.objects.filter(financialproduct__id=fpID.id)

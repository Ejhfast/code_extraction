# filtering fields of an inlineformset_factory
TourItemFormSet = inlineformset_factory(Tour,TourItem,can_delete=True,extra=4)
TourItemFormSet.form.base_fields["TourItemType"].queryset = TourItemType.objects.filter(Lang__iexact=request.LANGUAGE_CODE)
# then create an instance of TourItemFormSet and add to template context

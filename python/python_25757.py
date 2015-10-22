# How can I iterate inside a iteration with formfields?
StoreOpening = nestedformset_factory(StoreData,StoreOpening,nested_formset=nestedformset_factory(StoreOpening,OpeningDays,nested_formset=inlineformset_factory(StoreOpening, OpeningHours,extra = 0, can_delete=False), extra = 0, can_delete=False),extra = 0, can_delete=False)

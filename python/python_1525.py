# Handling an "Inventory" (complex associations) with django + appengine
character= get_object_or_404(Character, pk=character_id)
InventoryInlineFormSet = inlineformset_factory(Character, Inventory, max_num=1)
classificationformset = ClassificationInlineFormSet(instance=character)

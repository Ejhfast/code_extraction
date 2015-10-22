# django strip/remove/clear value
if not atype_config.LocalityDisplay:
    self.cleaned_data.pop('address_locality', None)

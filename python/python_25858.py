# django make ModelChoiceField non-editable
self.fields['field_name'].widget.attrs['disabled'] = 'disabled'

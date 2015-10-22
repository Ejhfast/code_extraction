# Remove empty level in django model form
if self.fields['place_of_first'].widget.choces[0][0] == "" :
    del self.fields['place_of_first'].widget.choices[0]

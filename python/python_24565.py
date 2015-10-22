# StrictButton at the bottom of a modelforms
self.helper.layout = Layout(
        *(self.Meta.fields + (StrictButton('Send', css_class='btn-default', type='submit'),))
    )

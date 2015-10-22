# How to re-use custom validation in Django?
class YourForm(forms.Form):
   ...
   image = forms.ImageField(validators=[validate_image_with_dimensions])

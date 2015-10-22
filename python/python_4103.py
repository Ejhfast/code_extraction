# How to create a personalized Django admin model?
class SimAdmin(admin.ModelAdmin):
    phone = forms.ModelChoiceField(queryset=Item.objects.filter(name='phone'))

# Django get instance in inline form admin
def get_formset(self, request, obj=None, **kwargs):
        InlineForm.obj = obj
        return super(InlineAdmin, self).get_formset(request, obj, **kwargs)

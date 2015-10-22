# How to Show Form Errors in Django Templates if wrong input is given in template only instantly?
def form_invalid(self, form):
    print form.errors
    return render(self.request, userdetailsView.template_name, {'result': '' ,  'form': form})

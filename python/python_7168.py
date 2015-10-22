# Django: CreateView fail_url
def form_invalid(self, form):
    return HttpResponseRedirect(self.get_success_url())

# Django Formsets: Prevent rendering an empty inline form
ArticleFormSet = formset_factory(ArticleForm, extra=2, max_num=1)

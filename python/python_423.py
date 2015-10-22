# Django: How to use stored model instances as form choices?
topics = forms.ModelMultipleChoiceField(queryset=BlogTopic.objects.all())

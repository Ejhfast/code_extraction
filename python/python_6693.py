# How do I set custom HTML attributes in django forms?
search_input = forms.CharField(_(u'Search word'), required=False)
search_input.widget = forms.TextInput(attrs={'size': 10, 'title': 'Search',})

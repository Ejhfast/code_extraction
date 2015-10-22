# How do I set a forms.CharField text programmatically?
for i, question in enumerate(extra):
            self.fields['custom_%s' % i] = forms.CharField(label=question)

# django ModelForm save() method issue
form = SnippetForm(data=request.POST, instance=snippet, force_update=True)

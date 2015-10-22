# How to get the label of a choice in a Django forms ChoiceField?
reason = form.cleaned_data['reason']
reason = dict(form.fields['reason'].choices)[reason]

# Django Form not posting due to TinyMCE removing name
description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False, label="Description")

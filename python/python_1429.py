# How to add clickable links to a field in Django admin?
def show_firm_url(self, obj):
    return '&lt;a href="%s"&gt;%s&lt;/a&gt;' % (obj.firm_url, obj.firm_url)
show_firm_url.allow_tags = True

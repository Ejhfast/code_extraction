# Django - random file in jquery in template
var js_array = [{% for f in filelist %}"{{ f }}",{% endfor %}];

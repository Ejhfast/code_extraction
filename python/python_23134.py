# Django templating system: Is there a way to render None as ''?
{{ instance.number|default_if_none:"" }}

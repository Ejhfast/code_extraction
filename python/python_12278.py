# Python/Django: Email template is not rendered. Shows html tags and doesn't convert entities
msg.attach_alternative(t.render(Context({})), "text/html")

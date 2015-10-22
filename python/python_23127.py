# Tornado reverse_url encodes 'special caracters' like ? and &
{{ reverse_url("web-html", "list-builds") + "?" + urlencode(dict(bundle_identifier=app.bundle_identifier)) }}

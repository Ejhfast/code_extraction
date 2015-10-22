# Flask: Get URLs for each View class in module
rules = app.url_map._rules
for rule in rules:
    print rule.endpoint, rule, rule.defaults

# regexp matching slug
compiled = re.compile(r'\d(?:-\d)*$')
result = compiled.match(string_to_parse)

# Edit XML value based on Key
foo_element = soup.find('macro', attrs={"name" : "foo"}) # returns the foo element
foo_element['value'] = "baz" # changes the value attribute

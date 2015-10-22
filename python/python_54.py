# Difflib.SequenceMatcher isjunk optional parameter query: how to ignore whitespaces, tabs, empty lines?
difflib.SequenceMatcher(lambda x: x in " \t\n", doc1, doc2).ratio()

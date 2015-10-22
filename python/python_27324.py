# Python SQLite how do you do partial searches using '?' placeholders?
q = '''SELECT * FROM MY_TABLE WHERE FIELD LIKE ?'''
some_query_value = '%test%'
cursor.execute(q, [some_query_value])

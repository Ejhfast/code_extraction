# DRY version of python if statements
for column in ('name', 'synopsis', 'something', 'other'):
    if not getattr(title, column):
        setattr(title, column, data[column])

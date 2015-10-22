# Python Pandas - Changing some column types to categories
for col in ['parks', 'playgrounds', 'sports', 'roading']:
    public[col] = public[col].astype('category')

# If column name is ____ then exclude it from DataFrame in Python
df[[c for c in df.columns if c not in ['X2','X3']]]

# Correct approach for calling a function regardless of parameter type
print_tables(int(user_input) if user_input.isdigit() else user_input)

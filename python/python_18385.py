# Python Regex - Match a character without consuming it
re.sub(r'\b(\s*)"(?!,|[ \t]*$)', r'\1""', s)

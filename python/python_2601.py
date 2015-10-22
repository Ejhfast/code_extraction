# Dynamically generating a generator function from a blob of text
exec "def f():\n " + " \n".join(code_string.splitlines()) + "\n"

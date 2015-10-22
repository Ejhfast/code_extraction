# Get backspace in python from stdin?
character = some_function_that_gets_a_character_from_stdin()
if character == '\x08' or character == '\x7f':
  do_smth()

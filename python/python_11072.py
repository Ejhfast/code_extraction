# How to match parentheses / brackets in pyparsing
delim_value = Group(delimitedList(string_value | int_value))("list")
list_value = Or( (Suppress("[") + delim_value + Suppress("]"),
                  Suppress("(") + delim_value + Suppress(")")) )

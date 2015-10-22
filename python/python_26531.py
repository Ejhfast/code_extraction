# Return True if all characters in a string are in another string
def only_uses_letters_from(string1, string2):
   """Check if the first string only contains characters also in the second string."""
   return set(string1) &lt;= set(string2)

# Python regular expressions with more than 100 groups?
newContents, num = cregex.subn(lambda m: replacements[m.string[m.start():m.end()]], contents)

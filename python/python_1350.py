# Regular Expression search/replace help needed, Python
re.sub(r"([aeiou])(t|k|s|tk)([^aeiou]*)$", r"\1:\2\3", "orchestras")
re.sub(r"([aeiou])(t|k|s|tk)$",            r"\1:\2",   "orchestras")

# Regex replacement
re.sub(r"(\{\{foobar[^\}]*)thisoption ?= ?xxx", r"\1thisoption = abc", string)

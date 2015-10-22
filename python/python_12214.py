# Python split string based on regex
l = re.compile("(?&lt;!^)\s+(?=[A-Z])(?!.\s)").split(s)

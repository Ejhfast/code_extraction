# Python's equivalent to PHP's strip_tags?
re.sub(r'&lt;[^&gt;]*?&gt;', '', value)

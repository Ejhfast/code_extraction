# Python regex - cleaning markdown html
re.sub(r'\s*(&lt;!--(?:[^-]+|-(?!-&gt;))*--&gt;)\s*', '\\n\\n\\1\\n\\n', yourstring)

# Python regular expression with wiki text
wikilink_rx = re.compile(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]')
return wikilink_rx.sub(r'\1', the_string)

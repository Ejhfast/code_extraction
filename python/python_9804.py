# Howto replace different values with tags in string?
import re
s = 'Lorem ipsum dolor [mytag]something[/mytag]sit amet, ipsum [mytag]something else[/mytag]a laoreet ultricies'
print re.sub(r'\[mytag\](.+?)\[/mytag\]', r'&lt;img src="\1"&gt;', s)

# Python regular expressions to stop when it sees an ampersand
$ my_text = re.search('(?&lt;=My\.Tag=)[^&amp;?]*', line)

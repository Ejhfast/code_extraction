# How to parse the file with international words in python
pat = re.compile(r'^(\d+\. |- |\*\* )?(?P&lt;word&gt;.*)')

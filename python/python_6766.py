# How to search for a word and then replace text after it using regular expressions in python?
re.sub(r'(&lt;form.*?action=")([^"]+)', r'\1newlogin.php',  content)

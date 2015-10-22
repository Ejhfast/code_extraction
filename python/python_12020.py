# UnicodeEncodeError when parsing month name with Python strptime
locale.setlocale(locale.LC_ALL, "deu_deu") # Locale name on Windows
datetime.strptime(dt.encode("iso-8859-16"), "%B %Y")

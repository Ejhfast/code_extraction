# Code not removing desired values from dictionary
cleanedText = [e.translate(remove_punctuation_map).lower() for e in text.split() if not e.startswith(('http', '@')) ]
shortenedText = [e for e in cleanedText if len(e) &gt;= 3]

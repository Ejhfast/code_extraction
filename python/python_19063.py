# Occurrences of a pattern in a string and its indices
pattern = "haha"
text = "hahahaha"
[i for i in range(len(text)-len(pattern)+1) if text[i:].startswith(pattern)]

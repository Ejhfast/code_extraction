# Parse URL from plain text
result = re.findall(r"\b(?:(?:https?|ftp|file)://|www\.|ftp\.)[-A-Z0-9+&amp;@#/%=~_|$?!:,.]*[A-Z0-9+&amp;@#/%=~_|$]", subject)

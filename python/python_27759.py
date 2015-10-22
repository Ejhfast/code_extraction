# Special characters not being replaced with regex
print re.sub(r'[^a-zA-Z0-9 +#-]+', '', text)

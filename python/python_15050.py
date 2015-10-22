# Find all html elements whose contains a specific class
soup.findAll(True, {'class': re.compile(r'\bsuper_class1\b')})

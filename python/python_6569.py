# Preserve space when stripping HTML with Beautiful Soup
print u' '.join(soup.findAll(text=True))

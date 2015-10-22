# Python - finding TTF files
def find_font_file(query):
       matches = filter(lambda path: query in os.path.basename(path), fontman.findSystemFonts())
       return matches

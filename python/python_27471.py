# NLTK can't open files (UnicodeDecoreError)
import io
io.open('harrypotter.txt', encoding='ISO-8859-1')  # Or other encoding of your file

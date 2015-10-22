# Unicode error when outputting python script output to file
import codecs
file = codecs.open("out.txt", "w", "utf-8")
file.write(something)

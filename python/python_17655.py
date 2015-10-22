# Getting an error in python at the time of file write
import codecs
with codecs.open('output.txt','w',encoding='utf8') as out:
    out.write(result)

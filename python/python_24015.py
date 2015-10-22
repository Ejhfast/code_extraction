# 'module' does not support the buffer interface
with open('1.gif') as fp:
    writeGif(fp, im, duration=0.1 )

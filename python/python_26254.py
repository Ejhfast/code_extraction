# MozJPEG STDIN Mode with switches
subp = subprocess.Popen(["/home/ubuntu/mozjpeg/cjpeg", "-quality","70"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
image_results = subp.communicate(input=out_im2.getvalue())

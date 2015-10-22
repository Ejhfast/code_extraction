# How to extract a filename from a URL & append a word to it?
filename = url[url.rfind("/")+1:]
filename_small = filename.replace(".", "_small.")

# splitting a path with python
filename = urlparse.urlparse(url).path.split('/')[-1]  # get file name
name = filename.rsplit('.', 1)[0] + '.html'  # change the extension

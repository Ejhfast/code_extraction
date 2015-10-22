# Is there a convenient way to map a file uri to os.path?
import os, urlparse
p = urlparse.urlparse('file://C:/test/doc.txt')
finalPath = os.path.abspath(os.path.join(p.netloc, p.path))

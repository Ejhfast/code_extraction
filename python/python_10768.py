# getting started with davlib.py
url = "davs://localhost:80/webdav/davtest.txt"
    r = ResourceStorer(url)
    result = r.downloadContent().read()

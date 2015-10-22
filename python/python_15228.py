# Using urllib to Download
download_url = ("Download link")
filename, headers = urllib.urlretrieve(download_url)
print filename

# How to download all pics in this website: huaban.com
image_path = 'http://img.hb.aicdn.com/3e32a8b101e515b9e7dbe8f5a2e47afff5ec6bcf4e4a-OTvsuu_fw192'
with open(r'&lt;path_to_file&gt;.jpg', 'wb') as image:
    image.write(urllib2.urlopen(image_path).read())

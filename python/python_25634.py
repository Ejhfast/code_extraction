# Replace wildcard from string
ex = "/Volumes/Obelix/5215.tif, /Volumes/Gemeinsam/25.tif, /Volumes/Obelix/5100.tif"
newex = re.sub(r'/Volumes/Gemeinsam/.+?,?(\s|$)', '', ex)

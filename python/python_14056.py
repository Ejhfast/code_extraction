# Write a regular expression to get a substring in Python
p = re.compile('\[.*\](\s.*\s)\[.*\].*\.jpg')
l = p.findall("[Anime-Koi] GJ-bu - 07 [h264-720p][A8557259].mkv-00_07_33_00001.jpg")
print l

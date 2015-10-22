# Regex: Replace one pattern with another
pattern = re.compile(r'(\d+)x(\d+)') # for st_srt
st_srt = re.sub(pattern, r'S\1E\2', st_srt)

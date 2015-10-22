# how to sort list of FileInfo in IronPython
fileInfos = list(DirectoryInfo(path).GetFiles())
fileInfos.sort(key=lambda f: f.CreationTime, reverse=True)

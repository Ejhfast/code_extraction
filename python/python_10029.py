# Remove everything before certain character in nested lists (Python)
NestedList = [["BLAHBLAH\Desktop","BLAHBLAH\Documents","BLAHBLAH\Vids"],["BLAHBLAH\Pics","BLAHBLAH\Folder","BLAHBLAH\Music"]]
output = [[os.path.basename(path) for path in li] for li in NestedList]

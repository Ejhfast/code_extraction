# How to properly write readdir in Fuse python?
tags = ["a", "b", "c"]
ret = map(lambda k: fuse.Direntry(name = k, type = stat.S_IFDIR), tags)
return ret

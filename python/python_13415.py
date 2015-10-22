# python (and AWS): having trouble sorting list of S3 keys by date
lst = sorted(lst, key=lambda kk: kk.last_modified, reverse=True)

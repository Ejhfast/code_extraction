# re.search() logically or two patterns in re.search()
tt = int(re.search(r"\?ent took (too long \()?(?P&lt;num&gt;\d+)",message).group('num'))

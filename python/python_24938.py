# merge paths with python, from /a/b/c + c/d to /a/b/c/d
os.path.join(os.path.split(p1)[0], p2)

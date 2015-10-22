# Can we do a smart-copy in Python?
# If more than 1 second difference
if os.stat(src).st_mtime - os.stat(dest).st_mtime &gt; 1:
    shutil.copy2 (src, dst)

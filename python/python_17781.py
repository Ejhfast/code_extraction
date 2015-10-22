# Recursive directory size includes symlinks twice
totalSize += os.path.getsize(fp) if not os.path.islink(fp) else 4096

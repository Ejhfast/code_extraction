# Scons Multi-Directory copying/zipping
target = "dir where you want to copy contents of source"
basedir = "source dir containing content to be copied"
env.Accumulate(target, [os.path.join(basedir ,x) for x in os.listdir(basedir)])

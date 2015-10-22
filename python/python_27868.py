# Run pdb from command line on application packaged as a zip file?
python -c 'import pdb, youtube_dl; print youtube_dl; pdb.runcall(youtube_dl.main, ["-h"])' youtube-dl

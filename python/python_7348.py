# Python Batch convert of flac files
for flacfiles in flacs:
    if os.path.exists(os.path.splitext(flacfiles)[0] + '.cue')):
        # do something

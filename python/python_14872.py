# Python BUG or I don't get how encoding works? len, find, and re.search do nothing with no empty, sucessfull subprocess.communicate() execution result
def get_video_duration (ifile):
    p = subprocess.Popen(["ffprobe", ifile], stderr=subprocess.PIPE)
    info_str = p.communicate()[1].decode(sys.stderr.encoding)

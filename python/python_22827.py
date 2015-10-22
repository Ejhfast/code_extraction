# ffmpeg Python Subprocess Error returned non-zero exit status 1
subprocess.check_output(["ffmpeg", "-i", self.moviefile, "-ss", "00:01:00.000", "-t", "00:00:05", "-vf", "scale=" + str(resolution) + ":-1", "-r", str(framerate), "-qscale:v", "6", self.processpath + "/" + self.filetitles + "-output%03d.jpg"])

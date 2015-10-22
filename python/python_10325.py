# Cannot run ffmpeg in subproces.call
ffmpeg_command = ["avconv", "-i", self.absolute_path]
    p = Popen(ffmpeg_command, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()

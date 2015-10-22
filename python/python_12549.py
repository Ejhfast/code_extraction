# pexpect.run() terminates before ending ffmpeg without finishing the conversion
output = file(LOG_FILE, 'a')
    args = shlex.split(self.command_video())
    return subprocess.call(args, stdout=output, stderr=output)

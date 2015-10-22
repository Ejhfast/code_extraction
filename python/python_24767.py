# How to run a shell script without having to press enter/confirm s.th. inbetween
import subprocess
subprocess.call(["xdotool","key","Return"])

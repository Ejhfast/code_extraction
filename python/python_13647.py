# How to change the shutdown message for Windows using python?
import subprocess
subprocess.call(["shutdown", "-f", "-r", "-t", "10", "-c", '"MESSAGE HERE"'])

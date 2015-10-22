# Running cmd in python (ffmpeg)
os.chdir('C://Users/Alex/')
subprocess.call(['ffmpeg', '-i', 'picture%d0.png', 'output.avi'])
subprocess.call(['ffmpeg', '-i', 'output.avi', '-t', '5', 'out.gif'])

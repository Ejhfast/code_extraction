# What tokens to use with Popen for running a blender script?
import subprocess
p = subprocess.Popen(["blender object.blend --background --python blenderObj.py --box.obj object.obj"], stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()

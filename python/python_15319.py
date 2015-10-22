# Using Unix command (node.js/lessc in my case) inside python?
import subprocess
p = subprocess.Popen(['lessc', '-x', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
output = p.communicate(less_content)

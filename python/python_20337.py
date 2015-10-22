# Launch Multiple copies of a program
import os
os.spawnl(os.P_NOWAIT, "./program1.py", "hello")

# How to Change DNS Servers Programmaticly in Windows with Python?
import os
os.system('netsh interface ip set dns "Local Area Connection" static 192.168.0.200')

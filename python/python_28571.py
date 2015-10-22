# How to close all windows7 folders using python
import subprocess
subprocess.call('nircmd.exe win close class "CabinetWClass"' , shell=True)

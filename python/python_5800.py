# How to execute long bash sequence with Python subprocess
subprocess.call('echo -e "root (hd0,1)\nfind /boot/grub/menu.lst\nsetup (hd0)\nquit" | grub --batch', shell=True)

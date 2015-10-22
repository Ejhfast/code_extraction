# 'python' command segmentation fault on raspberry pi
$ sudo apt-get install --reinstall `dpkg --get-selections | grep -E '^(lib)?python' | cut -f1 | cut -d: -f1`

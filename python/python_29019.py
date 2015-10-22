# Python syntax to open gnome-terminal and execute multiple commands
os.system("gnome-terminal -e 'bash -c \"sudo add-apt-repository ppa:x2go/ppa &amp;&amp; sudo apt-get update ; exec bash\"'")

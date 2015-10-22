# Traffic shaping under Linux
tc class add dev eth2 parent 1: classid 1:1 htb rate 100Mbit ceil 100Mbit quantum 1600

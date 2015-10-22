# Dumbo(Python)/Hadoop unexpected output
dumbo cat ipcounts/part* -hadoop /usr/local/hadoop | sort -k2,2nr | head -n 5

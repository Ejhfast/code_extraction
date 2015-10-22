# Finding login times in Linux
for f in /var/log/wtmp*; do last -f $f reboot;done

# Running a python script from crontab
* * * * * su esr -c "DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$(ps -au esr | grep -i "gnome-session" | awk '{ print $1 }')/environ | sed -e 's/DBUS_SESSION_BUS_ADDRESS=//') $(whereis notify-send | awk '{ print $2 }') -u normal -t 20000 \"Hello\" "

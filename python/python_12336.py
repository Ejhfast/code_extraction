# Python usbmount checking for device before writing
cat /etc/mtab | awk '{ print $2 }'

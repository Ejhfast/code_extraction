# Packets larger than MTU arriving on TUN interface
from pytun import TunTapDevice, IFF_TUN, IFF_NO_PI
tun = TunTapDevice(name="vpn",flags=(IFF_TUN | IFF_NO_PI))

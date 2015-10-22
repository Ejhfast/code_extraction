# iptables -I INPUT -p tcp --dport $PORT -i eth0 -m state --state NEW -m recent --update --seconds 600 --hitcount 2 -j DROP

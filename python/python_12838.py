# Video streaming over RTP using gstreamer
mpegparse ! rtpmpvpay ! udpsink host="hostipaddr" port="someport"

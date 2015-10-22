# Python Bencoding using BitTorrent-bencode 5.0.8.1
import bencode
print bencode.bdecode(open('file.torrent', 'rb').read())

# how do you make an IPv4 address printable with the getdnsapi python API?
bin_addr = results.reply_tree.reply[n]['answer']['rdata']['ipv4_address']
string_addr = '.'.join(map(str, map(ord, bin_addr)))

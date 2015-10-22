# 6 elements in an array but only showing up as 1
CellNetInfopkt += struct.pack("b" * len(this_or_address_send_array), *this_or_address_send_array)
#  Notice the "*"                                                   ^^^

# How to set the delivery time for new messages in mailbox?
msg.__setitem__('Date',
                time.strftime("%a, %d %b %Y %H:%M:%S %z",
                              entry_time))

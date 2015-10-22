# Is there any more compact way of writing that statement?
':'.join('%02x' % (i&gt;&gt;(8*j) &amp; 0xFF) for j in reversed(range(6)))

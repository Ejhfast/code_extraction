# How do you reverse the significant bits of an integer in python?
reversed_ = sum(1&lt;&lt;(numbits-1-i) for i in range(numbits) if original&gt;&gt;i&amp;1)

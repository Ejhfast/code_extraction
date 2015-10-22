# Why (0x7FFFFFFF >> 31) + 1 is zero?
$ echo $(( (0x7FFFFFFF &gt;&gt; 31) + 1 ))
1

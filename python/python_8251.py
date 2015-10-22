# How to convert a MAC number to MAC string?
&gt;&gt;&gt; ':'.join(s.encode('hex') for s in '00163e2fbab7'.decode('hex'))
'00:16:3e:2f:ba:b7'

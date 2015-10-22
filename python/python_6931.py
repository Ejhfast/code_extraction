# Regular expressions in python : don't split when a specific substring is found
&gt;&gt;&gt;x = 'ACD VU LSF VMSUGH VIJ SVD HJV DVO'
&gt;&gt;&gt;result = re.split('V[A-Z](?&lt;!SVD)', x)
['ACD ', ' LSF ', 'SUGH ', 'J SVD HJV D', '']

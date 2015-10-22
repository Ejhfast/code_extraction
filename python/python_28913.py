# Python regroup item in dictionary
&gt;&gt;&gt; li = ['paris', 'paris', 'marseille', 'marseille', 'marseille', 'paris', 'paris', 'paris', 'lille', 'marseille', 'toulouse', 'marseille', 'lille', 'mont saint martin', 'mont de marsan', 'lyon', 'lyon', 'lille', 'lille', 'lyon']
&gt;&gt;&gt; [c for e in li for c in e.split(" ")]

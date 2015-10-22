# How can I capture this through a regex?
&gt;&gt;&gt; re.match('(ABC|EFH)(PQR|STU)', 'ABCPQR01 is not at all good').groups()
('ABC', 'PQR')

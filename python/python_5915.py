# The opposite of string.Template in Python
&gt;&gt;&gt; re.match(r"\D*(\d+)\D+([\d\.]+)\D+([\d\.]+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)",
             "   123;  Coord   ;  19.1335;   3.5010;  1; 3; 8; 4").groups()
('123', '19.1335', '3.5010', '1', '3', '8', '4')

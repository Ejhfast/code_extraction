# Python: writing integers to a single byte
val = ((d &amp; 1) &lt;&lt; 7) | ((c &amp; 1) &lt;&lt; 6) | ((b &amp; 7) &lt;&lt; 3) | (a &amp; 7)

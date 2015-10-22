# Count elements in a box
count = ((min &lt; X) &amp; (X &lt; max) &amp;
         (min &lt; Y) &amp; (Y &lt; max) &amp;
         (min &lt; Z) &amp; (Z &lt; max)).sum()

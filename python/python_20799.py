# Python deal with date format like "1st, 2nd, 3rd, 4th"
&gt;&gt;&gt; re.sub(r"([0123]?[0-9])(st|th|nd|rd)",r"\1&lt;sup&gt;\2&lt;/sup&gt;","Meet you on 5th")
'Meet you on 5&lt;sup&gt;th&lt;/sup&gt;'

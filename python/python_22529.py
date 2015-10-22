# Regular Expression for Parsing Server Traceback
\[(?P&lt;timestamp&gt;.*?)\] (?P&lt;level&gt;\w+) \[(?P&lt;location&gt;.*?)\] (?P&lt;message&gt;.*?)\n(?P&lt;details&gt;.*?)(?=\n\[|$)

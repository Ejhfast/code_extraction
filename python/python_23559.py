# Python and regex: split a string with parenthesis
&gt;&gt;&gt; log = '[date] [thread] [loglevel] [class] some text describing the event that happened.'
&gt;&gt;&gt; [part.strip() for part in re.split('[\[\]]', log) if part.strip()]
['date', 'thread', 'loglevel', 'class', 'some text describing the event that happened.']

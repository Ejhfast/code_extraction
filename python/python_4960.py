# Method for parsing text Cc field of email header?
&gt;&gt;&gt; email.utils.getaddresses(['friend@email.com, John Smith &lt;john.smith@email.com&gt;,"Smith, Jane" &lt;jane.smith@uconn.edu&gt;'])
[('', 'friend@email.com'), ('John Smith', 'john.smith@email.com'), ('Smith, Jane', 'jane.smith@uconn.edu')]

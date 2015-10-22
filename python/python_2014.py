# python how to check file empty or not
&gt;&gt;&gt; import os
&gt;&gt;&gt; os.stat("file").st_size == 0
True

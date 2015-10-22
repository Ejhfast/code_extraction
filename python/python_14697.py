# Function to normalise string file paths
&gt;&gt;&gt; import os
&gt;&gt;&gt; print(os.path.normcase(os.path.normpath("C:\\abc/def/hij\\")))
c:\abc\def\hij

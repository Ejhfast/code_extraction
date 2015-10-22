# Extracting penultimate folder name from path
&gt;&gt;&gt; import os.path
&gt;&gt;&gt; os.path.basename(os.path.dirname("folderA/folderB/folderC/folderD"))
'folderC'

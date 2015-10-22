# Finding a GOP parameter value in video file using linux app and/or Python
ffmpeg -i &lt;FILENAME_HERE&gt; -vf showinfo -f rawvideo -y /dev/null 2&gt;&amp;1 | grep -i showinfo | awk '{print $4, $6, $12, $13}'

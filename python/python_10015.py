# How to get spacings around lists with Sphinx in the latexpdf output?
sed '/\\begin{itemize}/{x;p;x}' input &gt; output

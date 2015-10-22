# Python : The most efficient way to join two very big (20+ GB) datasets?
sort -o df_ns.csv df_ns.csv &amp;&amp; \
sort -o df_ip.csv df_ip.csv &amp;&amp; \
join -t'|' df_ns.csv df_ip.csv &gt; df_combined.csv

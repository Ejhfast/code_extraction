# set file permissions in one directory to match another
cd dir-a &amp;&amp; getfacl -R . &gt; /permissions.acl
cd dir-b &amp;&amp; setfacl --restore=/permissions.acl

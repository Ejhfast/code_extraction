# Executing reboot command over SSH using Paramiko
ssh.exec_command("/sbin/reboot -f &gt; /dev/null 2&gt;&amp;1 &amp;")

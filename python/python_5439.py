# Can I have subprocess.call write the output of the call to a string?
&gt;&gt;&gt; cmd = subprocess.Popen('ls', stdout=subprocess.PIPE)
&gt;&gt;&gt; cmd_out, cmd_err = cmd.communicate()

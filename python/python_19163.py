# Python Popen waiting while it shouldn't (bg and output redirected)
p = Popen('bash -c "echo \'useful\'; cd ~/dicp/python; nohup sleep 5 &amp;&gt; /tmp/out.txt &amp; echo \'more\';"', shell = True, stdout = PIPE, stderr = PIPE)
print p.communicate()

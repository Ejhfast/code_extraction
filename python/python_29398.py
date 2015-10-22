# Why would inspect.getfile give me a file that's not there?
salt 'my-minion' cmd.run "nohup /bin/sh -c 'sleep 10 &amp;&amp; salt-call --local service.restart salt-minion'"

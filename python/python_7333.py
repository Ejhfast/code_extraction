# jython killing parent process that spawns subprocess breaks subprocess stdout to file?
Popen(' '.join(args+['&gt;', 'logFile', '2&gt;&amp;1']), # shell specific cmdline
      shell=True) # on Windows see _cmdline2list to understand what is going on

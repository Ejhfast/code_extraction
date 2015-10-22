# Any way to issue telnet commands remotely ander double telnet session?
$ echo "echo -e 'command_1\ncommand_2\ncommand_3' | telnet localhost 1234" | telnet 1.1.1.1

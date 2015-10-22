# SSH into a server, run a command and save its output to a variable in Python
rem = SshMachine("hostname", user = "john", keyfile = "/path/to/idrsa")
output = rem.which("ls")

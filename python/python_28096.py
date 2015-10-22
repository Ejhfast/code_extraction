# Cannot do "sudo su - postgres" with subprocess.call
subprocess.call(['sudo su - postgres'], shell=True)

# How to call my fabfile within my Python script
import subprocess
subprocess.call(['fab', '-f', 'fabfile.py', '-u ec2-user', '-i', 'id_rsa', '-H', bakery_internalip, 'deploy'])

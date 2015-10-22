# How do I use Fabric to SSH to two different ports on the same server?
execute(secondSSH, hosts=["notmmaley@%s:8101" % h for h in env.hosts])

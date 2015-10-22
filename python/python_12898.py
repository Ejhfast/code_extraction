# Fabric Sudo No Password Solution
run('echo "{0} ALL=(ALL) ALL" &gt;&gt; /etc/sudoers'.format(env.user))

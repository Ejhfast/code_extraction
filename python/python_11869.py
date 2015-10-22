# find virtualenv current package directory for vim
nnoremap &lt;F7&gt; :!ctags -R --python-kinds=-i -a $VIRTUAL_ENV/lib/python2.7/site-packages/django/*

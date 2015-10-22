# Homebrew: PATH env var is modified before installation of Formulae (mercurial will use system python instead of homebrew python)
$ brew reinstall mercurial --build-from-source --env=std
$ head -n 1 /usr/local/bin/hg
#!/usr/local/opt/python/bin/python2.7

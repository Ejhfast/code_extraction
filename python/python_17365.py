# Python Import Error for modules installed with Homebrew
For non-homebrew python (2.x), you need to amend your PYTHONPATH like so:
export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH

# IPython Notebook doesn't see environment variables with "bash magic"
sudo echo "JYTHON_HOME=/usr/lib/jvm/jython" | sudo tee -a /etc/environment
source /etc/environment
export JYTHON_HOME=/usr/lib/jvm/jython

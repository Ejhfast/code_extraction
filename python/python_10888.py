# Turn Django list of paths into PYTHONPATH
export PYTHONPATH='/opt/app/current':`ls -d -1 /opt/app/current/eggs/* | tr '\n' ':'`

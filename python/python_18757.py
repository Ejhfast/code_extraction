# Error when trying to setting up the CKAN filestore with local storage: Permission Denied
sudo chown -R `whoami` /var/lib/ckan/default
sudo chmod -R u+rwx /var/lib/ckan/default

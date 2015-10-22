# nodejs give error Error initializing V8 on cent os
yum localinstall --nogpgcheck http://nodejs.tchol.org/repocfg/fedora/nodejs-stable-release.noarch.rpm
yum -y install nodejs nodejs-compat-symlinks
systemctl restart httpd.service

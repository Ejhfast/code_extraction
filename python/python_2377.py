# Python: How can I override one module in a package with a modified version that lives outside the package?
import local_django.conf
import django.conf
django.conf.settings = local_django.conf.settings

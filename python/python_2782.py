# How do I suppress "unused in wild import" warning in pydev?
from django.db import connection #@UnusedImport
from django.db import * #@UnusedWildImport

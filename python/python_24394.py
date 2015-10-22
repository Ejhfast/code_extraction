# How to script django shell operations?
echo "from myapp.scenarios import *; reset_demo_data(); exit()" | python manage.py shell

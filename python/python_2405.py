# Hudson "Source code is unavailable."
coverage run manage.py test
coverage xml
sed 's/filename="/filename="my\/path\//g' coverage.xml &gt; coverage2.xml

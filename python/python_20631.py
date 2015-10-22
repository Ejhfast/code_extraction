# Run a django shell in batch file with script
echo "from myapp.model import Contact; c = Contact.objects.all().count(); print c" | python manage.py shell

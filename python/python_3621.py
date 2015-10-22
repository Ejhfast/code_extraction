# How would I use a South migration to load data into Django's auth_group table?
def forwards(self, orm):
    from django.core.management import call_command
    call_command("loaddata", "my_fixture.json")

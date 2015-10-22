# How to run periodic celery task manually from terminal in pyramid?
from views.celerytasks.mytask1 import my_mega_task_number_one
my_mega_task_number_one.delay()

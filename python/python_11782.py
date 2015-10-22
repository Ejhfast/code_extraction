# Sort Django objects by method with arguments
user = User.objects.get(username="jamie")
sorted(Task.objects.all(), key = lambda task, user=user: task.date_for_display(user))

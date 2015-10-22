# Quering Embedded Documents using MongoEngine in django, python
results = Lesson.objects(__raw__={'subject.subject_name': 'Math'})

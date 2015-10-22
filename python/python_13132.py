# mongoengine - Use QuerySet as ReferenceField
john_from_db = User.objects(email='jdoe@example.com').first()

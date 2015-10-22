# django.db.utils.IntegrityError: duplicate key value violates unique constraint "django_content_type_pkey"
SELECT setval('django_content_type_id_seq', (SELECT MAX(id) FROM django_content_type));

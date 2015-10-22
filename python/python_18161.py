# Using mock to patch a celery task in Django unit tests
with patch('myapp.myview.mytask.delay') as mock_task:

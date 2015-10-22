# Error R11 (Bad bind) -> Process bound to port 8000, should be 25162 (see environment variable PORT)
web: python my_app/manage.py run_gunicorn -b "0.0.0.0:$PORT"

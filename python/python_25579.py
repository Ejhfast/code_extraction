# How to create test database with Flask-Testing
app = Flask(__name__)
app.config.from_pyfile('base')
app.config.from_envvar('YOURAPPLICATION_SETTINGS')

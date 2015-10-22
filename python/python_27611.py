# How to fix itsdangerous.BadTimeSignature Signature Error
from itsdangerous import URLSafeTimedSerializer
app.secret_key = gen_random_key()
login_serializer = URLSafeTimedSerializer(app.secret_key)

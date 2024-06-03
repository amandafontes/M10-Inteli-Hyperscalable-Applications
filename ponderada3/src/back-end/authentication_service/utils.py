import jwt
from datetime import datetime, timedelta

def generate_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, 'your_secret_key', algorithm='HS256')

def validate_token(token):
    try:
        payload = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None

import os
from datetime import datetime, timedelta
import jwt
from typing import Optional
from decouple import config
from typing import Dict
from passlib.context import CryptContext
SECRET: str = config("SECRET_KEY", cast=str)
ALGORITHM: str = config("ALGORITHM", cast=str ,default="HS256")

def create_access_token(user_id:int, role:str, expiretime:int) -> Dict[str,str]:
    payload = {
        "sub": user_id,
        "role":role,
        "exp": datetime.utcnow() + timedelta(minutes=expires_minutes)
        }
    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
    
    return token

def decode_access_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
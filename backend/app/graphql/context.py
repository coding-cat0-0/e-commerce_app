from auth.handler import decode_access_token
from .database import get_session
from functools import wraps
async def get_context(request):
    
    user = None
    token = None
    session = get_session()

    auth = request.headers.get("Authorization")
    if auth and auth.startswith("Bearer "):
        token = auth.split(" ")[1]
        payload = decode_access_token(token)
        if payload:
            user = payload  

    return {
        "request": request,
        "user": user,
        "token": token,
        "session": session,
    }
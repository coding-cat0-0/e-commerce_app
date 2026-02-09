from auth.auth_handler import decode_access_token
from database import get_session, engine
from functools import wraps
from fastapi import HTTPException, status
from fastapi.requests import Request
from sqlmodel import Session, select
async def get_context(request: Request):
    
    user = None
    token = None
    with Session(engine) as session:
        auth = request.headers.get("Authorization")
        
        if auth and auth.startswith("Bearer "):
            token = auth.split(" ")[1]
            try:
                payload = decode_access_token(token)
                if payload:
                    user = payload
            except Exception:
                raise HTTPException(status_code=401, detail="Invalid or expired token")

        return {
            "request": request,
            "user": user,
            "token": token,
            "session": session,
        }
from fastapi import HTTPException
import jwt, pytz
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta
from app.User.models.User import User
from sqlalchemy.orm import Session
from app.Constants.constants import JWT_TOKEN_SECRET_KEY, JWT_ALGORITHM



def create_token(user: User):
    to_encode = {"sub": str(user.id), "exp": datetime.now(pytz.utc) + timedelta(minutes=30)}
    return jwt.encode(to_encode, JWT_TOKEN_SECRET_KEY, algorithm=JWT_ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, JWT_TOKEN_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload.get("sub")
    except ExpiredSignatureError as e:
        raise HTTPException(status_code=401, detail="Admin Token expired")
    except InvalidTokenError as e:
        raise HTTPException(status_code=401, detail="Admin Token invalid")

def authenticate_admin(db: Session, email: str, password: str):

    user = db.query(User).filter(User.email == email, User.is_admin == True).first()
    if user and user.password == password:
        return user
    
    return None

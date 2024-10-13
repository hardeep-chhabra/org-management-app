from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import *
from app.Authentication.AuthService import *
from app.User.UserService import *
from app.db import get_db
from fastapi.responses import JSONResponse


router = APIRouter()


@router.post("/login")
async def admin_login(admin: AdminLogin, db: Session = Depends(get_db)):
    
    user = authenticate_admin(db, admin.email, admin.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_token(user)
    return {"token": token}


@router.post("/user/create")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):

    admin_user_id = verify_token(user.token)
    return JSONResponse(content=create_user_func(db, user, admin_user_id), media_type="application/json")

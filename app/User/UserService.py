from sqlalchemy.orm import Session, joinedload
from app.User.models.User import User
from app.User.schemas import UserCreate
from sqlalchemy.exc import SQLAlchemyError
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException


def create_user_func(db: Session, user: UserCreate, admin_user_id: int):
    try:
        user_obj = db.query(User).filter(User.id == admin_user_id).options(joinedload(User.organization)).first()
        organization_obj = user_obj.organization
        new_user = User(email=user.email, password=user.password, organization_id=organization_obj.id)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return jsonable_encoder(new_user.to_dict())
    
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
from sqlalchemy.orm import Session
from app.Organization.models.Organization import Organization
from sqlalchemy.exc import SQLAlchemyError
from app.Organization.schemas import OrganizationCreate
from fastapi import HTTPException
from app.User.models.User import User



def create_organization_func(db: Session, org: OrganizationCreate):

    try:
        new_org = Organization(name=org.organization_name)
        db.add(new_org)
        db.commit()
        db.refresh(new_org)

        # Create admin user
        new_admin = User(email=org.email, password=org.password, is_admin=True, organization_id=new_org.id)
        db.add(new_admin)
        db.commit()
        return new_org
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_organization_by_name(db: Session, name: str):
    return db.query(Organization).filter(Organization.name == name).first()

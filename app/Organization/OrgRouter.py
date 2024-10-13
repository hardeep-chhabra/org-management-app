from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from .schemas import *
from fastapi.encoders import jsonable_encoder
from .OrgService import *
from app.db import get_db

router = APIRouter()


@router.post("/create", response_model=OrganizationCreate)
async def create_organization(org: OrganizationCreate, db: Session = Depends(get_db)):

    organization_obj = create_organization_func(db, org)
    return JSONResponse(content=jsonable_encoder(organization_obj.to_dict()), media_type="application/json")


@router.get("/get")
async def get_organization(org: OrganizationGetDetails, db: Session = Depends(get_db)):
    
    organization = get_organization_by_name(db, org.org_name)
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    return organization

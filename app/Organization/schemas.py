from pydantic import BaseModel, Field
from typing import Optional


class OrganizationCreate(BaseModel):
    email: str
    password: str
    organization_name: str


class OrganizationGetDetails(BaseModel):
    org_name: str = Field(..., alias="organization_name")

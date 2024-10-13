from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)
    organization_id: Mapped[int] = mapped_column(ForeignKey("organization.id"), nullable=False)
    organization = relationship("Organization", backref="users")


    def to_dict(self):
        return {
            "id": self.id, 
            "email": self.email, 
            "password": self.password, 
            "is_admin": self.is_admin, 
            "organization_id": self.organization_id
        }
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db import Base


class Organization(Base):
    __tablename__ = "organization"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

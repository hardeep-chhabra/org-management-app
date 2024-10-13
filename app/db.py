from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


database_credentials = {
    'POSTGRESUSER': 'hardeepchhabra',
    'PASSWORD': '12345',
    'HOST': 'db',
    'PORT': '5432',
    'DATABASE': 'organization_management'
}


SQLALCHEMY_DATABASE_URL = f"postgresql://{database_credentials['POSTGRESUSER']}:{database_credentials['PASSWORD']}@{database_credentials['HOST']}:{database_credentials['PORT']}/{database_credentials['DATABASE']}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

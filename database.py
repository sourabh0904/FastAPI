import os
from dotenv import load_dotenv
from sqlmodel import SQLModel , create_engine , Session

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

def create_db():
    """Create all tables defined by SQLModel"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Create a new database session"""
    with Session(engine) as session:
        yield session
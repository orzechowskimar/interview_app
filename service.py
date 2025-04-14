from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate
import logging

logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate):
        logger.info(f"Creating user: {user.username}")
        db_user = User(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_users(self, skip: int = 0, limit: int = 10):
        logger.info(f"Fetching users: skip={skip}, limit={limit}")
        return self.db.query(User).offset(skip).limit(limit).all()
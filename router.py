from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import logging

from database import get_db
from schemas import UserCreate, UserOut
from service import UserService

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        logger.info(f"POST /users - payload: {user}")
        return UserService(db).create_user(user)
    except ValueError as e:
        logger.warning(f"Validation error: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.get("/", response_model=list[UserOut])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        logger.info(f"GET /users?skip={skip}&limit={limit}")
        return UserService(db).get_users(skip, limit)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
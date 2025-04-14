from pydantic import BaseModel, constr, EmailStr

class UserCreate(BaseModel):
    username: constr(strip_whitespace=True, min_length=1, max_length=50)
    email: EmailStr

class UserOut(UserCreate):
    id: int

    class Config:
        orm_mode = True
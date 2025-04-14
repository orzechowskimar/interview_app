from fastapi import FastAPI
import logging
import uvicorn
from database import engine, Base
from router import router as user_router

# logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),       # log to file
        logging.StreamHandler()               # log to console
    ]
)
app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(user_router, prefix="/users", tags=["users"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
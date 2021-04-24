# do something about the root visit.
from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def root():
    return {"message": "welcome to facegame, have fun!"}
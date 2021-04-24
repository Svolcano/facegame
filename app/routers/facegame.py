# all api about the facegame
from fastapi import APIRouter
import uuid
from pydantic import BaseModel
from utils.utils import (gen_facegame, game_judge, is_win, get_best_score,
                         is_valid_game, get_all, save_record)


class GameRecordItem(BaseModel):
    game_id: str
    score: int
    detail: str
    cur_state: str
    start_date: str
    end_date: str


router = APIRouter(
    prefix="/facegame",
    tags=["facegame"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/", tags=["facegame"])
async def init():
    game_id = uuid.uuid4()
    new_game_data = gen_facegame()
    save_record(game_id, new_game_data)
    return {
        "game_id": game_id,
        "best": get_best_score(),
        "game_data": new_game_data,
    }


@router.get("/{game_id}/{index}", tags=["facegame"])
async def read_users(index: int, game_id: str):
    valid, msg = is_valid_game(game_id, index)
    if not valid:
        return {"error": msg}
    return {
        "game_id": game_id,
        "best": get_best_score(),
        "game_data": game_judge(game_id, index),
        "is_win": is_win(game_id),
    }


@router.get("/all", tags=["facegame"])
async def get_all_data():

    return {
        "game_id": '',
        "best": get_best_score(),
        "game_data": get_all(),
        "is_win": '',
    }
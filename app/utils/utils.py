# tools for the app

import random
import json
import time

from settings import (CARD_NUM, CHOICES, CARD_STATE_DOWN, CARD_STATE_UP, GAMES,
                      GAMES_RECORDS, GAME_STATE_OVER, GAME_STATE_STARTED, GAME_TIMEOUT)


def gen_facegame() -> dict[int, tuple[int, str]]:
    '''
    generate game init data.
    like : a = {
        1: [1, 1],
        2: [3, 1],
        ...
        12:[3, 1],
    }
    '''

    result = {}
    input = CHOICES * 2
    i = 1
    while i <= CARD_NUM:
        result[i] = [
            input.pop(random.randint(0,
                                     len(input) - 1)), CARD_STATE_DOWN
        ]
        i += 1
    return result


def game_judge(game_id: str, index: int) -> dict[int, tuple[int, str]]:
    '''
    game_id:str , like 11-22-33-44, used for get current game states: 
    like {
        1:[1, 0],
        2:[3, 0],
        3:[4, 1],
        ...
        12:[6, 1],
    }
    index: the next hit index [1, 12]
    '''
    cur_state = json.loads(GAMES_RECORDS[game_id]['detail'])
    GAMES_RECORDS[game_id]['end_time'] = time.time()
    number, state = cur_state.get(index, (None, None))
    if number is None:
        return cur_state
    for card_index in cur_state:
        if index == card_index:
            continue
        n, s = cur_state[card_index]
        if n == number and s == CARD_STATE_UP:
            cur_state[index][1] = CARD_STATE_UP
            # found paird card, update the hited card's state and return updated card_states
            return cur_state
    # do nothing
    return cur_state


def is_win(game_id: str) -> bool:
    '''
    game_id:str , like 11-22-33-44, used for get current game states: 
    like {
        1:[1, 0],
        2:[3, 0],
        3:[4, 1],
        ...
        12:[6, 1],
    }
    '''
    cur_state = json.loads(GAMES_RECORDS[game_id]['detail'])
    up_card_num = 0
    for card_index in cur_state:
        n, s = cur_state[card_index]
        if s == CARD_STATE_UP:
            up_card_num += 1
    return up_card_num == CARD_NUM


def get_best_score():
    return 100


def is_valid_game(game_id: str, index: int) -> tuple[bool, str]:
    if game_id in GAMES_RECORDS:
        record = GAMES_RECORDS[game_id]
        if record['state'] == GAME_STATE_STARTED:
            if index >= 1 and index <= CARD_NUM:
                now = time.time()
                if now - record['end_time'] > GAME_TIMEOUT:
                    return False, "overtime"
                return True, "valid"
            else:
                return False, 'index error'
        else:
            return False, 'state, error'
    else:
        return False, 'not exists'


def save_record(game_id: str,
                game_data: dict[int, tuple[int, str]],
                score: int = 0,
                end_time: float = 0,
                state: int = GAME_STATE_STARTED) -> bool:
    record = {
        'game_id': game_id,
        'detail': json.dumps(game_data),
        'score': score,
        'start_time': time.time(),
        'end_time': end_time,
        'state': state
    }
    GAMES_RECORDS[game_id] = record
    return True

def get_all():
    return GAMES_RECORDS

if __name__ == '__main__':
    r = gen_facegame()
    print(r)

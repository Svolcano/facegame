# settings for the app

CHOICES = [1, 2, 3, 4, 5, 6]
CARD_NUM = len(CHOICES) * 2

CARD_STATE_UP = 1
CARD_STATE_DOWN = 0

GAME_STATE_STARTED = 0
GAME_STATE_OVER = 1
GAME_TIMEOUT = 30 * 60   # 30 min

# fake db
GAMES_RECORDS = {
    '11-22-33-44': {
        'game_id': '11-22-33-44',
        'detail':{}, #  {:[1, 0],2:[3, 0],3:[4, 1],...12:[6, 1]} json str
        'score': 45,
        'start_time': 1111111111,
        'end_time': 1111111111,
        'state':GAME_STATE_STARTED
    }
    
}
GAMES = {
    'play_game_counter':1000, 
    'best_score':99,
}

NAME = 'PLV'
STANDARD_SCREEN_SIZE = (600, 400)
STANDARD_BG_COLOR = (255, 255, 255)
SCREEN_COUNT = 0
ANIMATION_STATUSES = {
    0: 'STAY_R',
    1: 'STAY_L',
    2: 'RUN_R',
    3: 'RUN_L',
    4: 'JUMP_R',
    5: 'JUMP_L',
    6: 'HIT_R',
    7: 'HIT_L',
    8: 'HIT_JUMP_R',
    9: 'HIT_JUMP_L',
    10: 'KICK_R',
    11: 'KICK_L',
    12: 'KICK_JUMP_R',
    13: 'KICK_JUMP_L'
}
HEALTH_POINTS = 100
DAMAGE = 20
BODY_INERTION = 0
FRAME_COUNTS = {
    'frame_run': 0,
    'stay': 0,
    'frame_jump': 0,
    'frame_hit': 0,
    'frame_kick': 0
}
STATUS_INTERPRETATION = {
    'frame_run': 'hit_box',
    'stay': 'hit_box',
    'frame_jump': 'hit_box',
    'frame_kick': 'damage_box',
    'frame_hit': 'damage_box'
}
STATUS_SEE = {
    'R': 50,
    'L': -50
}

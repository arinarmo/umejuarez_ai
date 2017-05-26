from pykeyboard import PyKeyboard
k = PyKeyboard()

BUTTONS = {
    "LP": 'a',
    "MP": "s",
    "HP": "d",
    "LK": "z",
    "MK": "x",
    "HK": "c",
    "L": k.left_key,
    "R": k.right_key,
    "U": k.up_key,
    "D": k.down_key
}

COMMAND_NORMALS = [
    [BUTTONS["R"], BUTTONS["HP"]],  # f.HP (L)
    [BUTTONS["L"], BUTTONS["HP"]],  # f.HP (R)
    [BUTTONS["R"], BUTTONS["MP"]],  # f.MP (L)
    [BUTTONS["L"], BUTTONS["MP"]],  # f.MP (R)
]

SPECIALS = [
    # Hadoken
    [[BUTTONS["D"]], [BUTTONS["D"], BUTTONS["R"]], [BUTTONS["R"], BUTTONS["LP"]]],  # light (L)
    [[BUTTONS["D"]], [BUTTONS["D"], BUTTONS["R"]], [BUTTONS["R"], BUTTONS["MP"]]],  # medium (L)
    [[BUTTONS["D"]], [BUTTONS["D"], BUTTONS["R"]], [BUTTONS["R"], BUTTONS["HP"]]],  # hard (L)
    [[BUTTONS["D"]], [BUTTONS["D"], BUTTONS["L"]], [BUTTONS["L"], BUTTONS["LP"]]],  # light (R)
    [[BUTTONS["D"]], [BUTTONS["D"], BUTTONS["L"]], [BUTTONS["L"], BUTTONS["MP"]]],  # medium (R)
    [[BUTTONS["D"]], [BUTTONS["D"], BUTTONS["L"]], [BUTTONS["L"], BUTTONS["LP"]]],  # hard (R)
    # Shoryuken
    [[BUTTONS["D"]], [BUTTONS["R"]], [BUTTONS["D"], BUTTONS["R"], BUTTONS["LP"]]],  # light (L)
    [[BUTTONS["D"]], [BUTTONS["R"]], [BUTTONS["D"], BUTTONS["R"], BUTTONS["MP"]]],  # medium (L)
    [[BUTTONS["D"]], [BUTTONS["R"]], [BUTTONS["D"], BUTTONS["R"], BUTTONS["HP"]]],  # hard (L)
    [[BUTTONS["D"]], [BUTTONS["L"]], [BUTTONS["D"], BUTTONS["L"], BUTTONS["LP"]]],  # light (R)
    [[BUTTONS["D"]], [BUTTONS["L"]], [BUTTONS["D"], BUTTONS["L"], BUTTONS["MP"]]],  # medium (R)
    [[BUTTONS["D"]], [BUTTONS["L"]], [BUTTONS["D"], BUTTONS["L"], BUTTONS["HP"]]],  # hard (R)
    # Tatsu
    [[BUTTONS["D"]], [BUTTONS["D"], BUTTONS["L"]], [BUTTONS["L"], BUTTONS["LK"]]],  # light (L)
    [[BUTTONS["D"]], [BUTTONS["D"], BUTTONS["L"]], [BUTTONS["L"], BUTTONS["MK"]]],  # medium (L)
    [[BUTTONS["D"]], [BUTTONS["D"], BUTTONS["L"]], [BUTTONS["L"], BUTTONS["HK"]]],  # hard (L)
    [[BUTTONS["D"]], [BUTTONS["D"], BUTTONS["R"]], [BUTTONS["R"], BUTTONS["LK"]]],  # light (R)
    [[BUTTONS["D"]], [BUTTONS["D"], BUTTONS["R"]], [BUTTONS["R"], BUTTONS["MK"]]],  # medium (R)
    [[BUTTONS["D"]], [BUTTONS["D"], BUTTONS["R"]], [BUTTONS["R"], BUTTONS["LK"]]],  # hard (R)

]

STANCES = {
    "standing": [], # standing
    "move_left": [BUTTONS["L"]],  # guard/move left
    "move_right": [BUTTONS["R"]],  # guard/move right
    "guard_low_left": [BUTTONS["L"], BUTTONS["D"]],  # guard low left
    "guard_low_right": [BUTTONS["R"], BUTTONS["D"]],  # guard low right
    "jump_neutral": [BUTTONS["U"]],  # neutral jump
    "jump_right": [BUTTONS["U"], BUTTONS["R"]], # jump right
    "jump_left": [BUTTONS["U"], BUTTONS["L"]]  # jump left
}


NORMALS = [
    [[BUTTONS["LP"]]],
    [[BUTTONS["MP"]]],
    [[BUTTONS["HP"]]],
    [[BUTTONS["LK"]]],
    [[BUTTONS["MK"]]],
    [[BUTTONS["HK"]]]
]
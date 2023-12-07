import pyxel

BrickType = {
    1: {
        "img": 0,
        "u": 16,
        "v": 0,
        "w": 32,
        "h": 8,
        "score": 1
    },
    2: {
        "img": 0,
        "u": 16,
        "v": 8,
        "w": 32,
        "h": 8,
        "score": 3
    },
    3: {
        "img": 0,
        "u": 16,
        "v": 16,
        "w": 32,
        "h": 8,
        "score": 5
    },
    4: {
        "img": 0,
        "u": 16,
        "v": 24,
        "w": 32,
        "h": 8,
        "score": 7
    },
}


class Brick:
    def __init__(self, x, y, brick_type):
        self.x = x
        self.y = y
        self.brick_type = brick_type
        self.w = BrickType[brick_type]["w"]
        self.h = BrickType[brick_type]["h"]
        self.score = BrickType[brick_type]["score"]

    def draw(self):
        pyxel.blt(
            self.x,
            self.y,
            BrickType[self.brick_type]["img"],
            BrickType[self.brick_type]["u"],
            BrickType[self.brick_type]["v"],
            BrickType[self.brick_type]["w"],
            BrickType[self.brick_type]["h"]
        )


def check_levels():
    found_levels = []
    with open("assets/levels.txt") as f:
        for line in f:
            found_levels.append(line.rstrip())
    return found_levels


def load_level(level):
    this_level = []
    possible_bricks = ["1", "2", "3", "4"]
    # Load the level file, and read through it, adding bricks to this_level
    with open("assets/" + level) as f:
        y = 0
        for line in f:
            x = 0
            for char in line:
                if char in possible_bricks:
                    this_level.append(Brick(x, y, int(char)))
                x += 32
            y += 8
    return this_level

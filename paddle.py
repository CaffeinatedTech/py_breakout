import pyxel


class Paddle:
    def __init__(self):
        self.w = 48
        self.h = 8
        self.x = pyxel.width / 2 - self.w / 2
        self.y = pyxel.height - 50
        self.mid_sections = 4
        self.sprite_img = 0
        self.sprite_w = 8
        self.sprite_end_u = 8
        self.sprite_end_v = 0
        self.sprite_mid_u = 0
        self.sprite_mid_v = 8

    def draw(self):
        pyxel.blt(
            self.x,
            self.y,
            self.sprite_img,
            self.sprite_end_u,
            self.sprite_end_v,
            self.sprite_w,
            self.sprite_w
        )
        for i in range(0, self.mid_sections):
            pyxel.blt(
                self.x + self.sprite_w + (self.sprite_w * i),
                self.y,
                self.sprite_img,
                self.sprite_mid_u,
                self.sprite_mid_v,
                self.sprite_w,
                self.sprite_w
            )
        pyxel.blt(
            self.x + self.sprite_w + self.sprite_w * self.mid_sections,
            self.y,
            self.sprite_img,
            self.sprite_end_u,
            self.sprite_end_v,
            self.sprite_w * -1,
            self.sprite_w
        )

    def update(self):
        # Move the paddle left and right based on the mouse location - clamp it to the edges of the game field
        self.x = min(pyxel.width - self.w, max(0, pyxel.mouse_x))

    def deflect_force(self, u):
        # Return the deflect force of the ball on the paddle
        force = (u - (self.x + self.w / 2)) / 10
        return force

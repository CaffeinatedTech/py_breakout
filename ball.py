import pyxel
from math import copysign, ceil


class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speedX = 2.0
        self.speedY = -1.5
        self.r = 2
        self.out_of_bounds = False

    def draw(self):
        pyxel.circ(self.x, self.y, self.r, 7)

    def update(self):
        # Move the ball, then check if it should bounce
        self.x += self.speedX
        self.y += self.speedY
        if self.x + self.r >= pyxel.width:
            self.speedX = self.speedX * -1
        elif self.y - self.r <= 0:
            self.speedY = self.speedY * -1
        elif self.x - self.r <= 0:
            self.speedX = self.speedX * -1
        elif self.y - self.r > pyxel.height:
            self.out_of_bounds = True

    def speedup(self, amount):
        self.speedX += copysign(amount, self.speedX)
        self.speedY += copysign(amount, self.speedY)

    def detect_collision(self, obj, paddle=False):
        score = 0
        # Calculate the number of sub-steps for the continuous collision detection
        num_steps = ceil(max(abs(self.speedX), abs(self.speedY)))
        if num_steps == 0:
            return False, score  # Ball is not moving

        # Calculate the step size for each sub-segment
        step_size = 1.0 / num_steps

        # Check for collisions along the sub-segments
        for step in range(1, num_steps + 1):
            t = step * step_size  # Interpolation factor between the start and end of the sub-segment
            sub_ball_x = self.x + t * self.speedX
            sub_ball_y = self.y + t * self.speedY

            # Check if the sub-segment collides
            if (
                sub_ball_x + self.r >= obj.x
                and sub_ball_x - self.r <= obj.x + obj.w
                and sub_ball_y + self.r >= obj.y
                and sub_ball_y - self.r <= obj.y + obj.h
            ):
                # Deflect the ball
                if paddle:
                    self.speedX = obj.deflect_force(self.x)
                    self.speedY = self.speedY * -1
                elif sub_ball_x + self.r >= obj.x > sub_ball_x - self.r:
                    # Ball hit left side of brick
                    self.x = obj.x - self.r
                    self.speedX = self.speedX * -1
                    score = obj.score
                elif sub_ball_x - self.r <= obj.x + obj.w < sub_ball_x + self.r:
                    # Ball hit right side of brick
                    self.x = obj.x + obj.w + self.r
                    self.speedX = self.speedX * -1
                    score = obj.score
                elif sub_ball_y + self.r >= obj.y > sub_ball_y - self.r:
                    self.y = obj.y - self.r
                    self.speedY = self.speedY * -1
                    score = obj.score
                elif sub_ball_y - self.r <= obj.y + obj.h < sub_ball_y + self.r:
                    self.y = obj.y + obj.h + self.r
                    self.speedY = self.speedY * -1
                    score = obj.score
                return True, score  # Collision detected
        return False, score  # No collision detected

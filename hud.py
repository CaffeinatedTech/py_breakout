import pyxel


def draw_hud(score=0, lives=0):
    # Draw score
    pyxel.text(10, 5, "Score: " + str(score), 7)
    # Draw lives
    lives_text = "Lives: " + str(lives)
    pyxel.text(right_text(lives_text), 5, lives_text, 7)


def draw_dropped():
    title = "DROPPED THE BALL"
    subtitle = "Click or Space to continue"
    pyxel.text(center_text(title), pyxel.height / 3, title, 7)
    pyxel.text(center_text(subtitle), pyxel.height / 2, subtitle, 7)


def draw_game_over(score=0):
    title = "GAME OVER"
    score_text = "you scored: " + str(score) + " points"
    press_enter_text = "Press ENTER to try again"
    pyxel.text(center_text(title), pyxel.height / 3, title, 7)
    pyxel.text(center_text(score_text), pyxel.height / 12 * 5, score_text, 7)
    pyxel.text(center_text(press_enter_text), pyxel.height / 2, press_enter_text, 7)


def draw_win(score=0):
    title = "YOU WIN"
    score_text = "you scored: " + str(score) + " points"
    press_enter_text = "Press ENTER to try again"
    pyxel.text(center_text(title), pyxel.height / 3, title, 7)
    pyxel.text(center_text(score_text), pyxel.height / 12 * 5, score_text, 7)
    pyxel.text(center_text(press_enter_text), pyxel.height / 2, press_enter_text, 7)

# Helper function for calculating the start x value for centered text.
def center_text(text, char_width=pyxel.FONT_WIDTH):
    text_width = len(text) * char_width
    return (pyxel.width - text_width) / 2


# Helper function for calculating the start x value for right aligned text.
def right_text(text, char_width=pyxel.FONT_WIDTH):
    text_width = len(text) * char_width
    return pyxel.width - (text_width + char_width)

import arcade

WIDTH = 640
HEIGHT = 480
player_x = 100
player_y = 100
fish = arcade.Sprite("images/fish.png", 0.1)
playerlist = None

# controls
up_pressed  = False
down_pressed = False
right_pressed = False
left_pressed = False

playerlist = arcade.SpriteList()

def update(delta_time):
    global player_y, player_x
    if up_pressed:
        player_y += 7
    elif down_pressed:
        player_y -= 7
    elif right_pressed:
        player_x += 7
    elif left_pressed:
        player_x -= 7

    if player_x == 0:
        player_x += 7
    elif player_x == WIDTH:
        player_x -= 7

def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_xywh_rectangle_filled(0, 0, 640, 480, arcade.color.SKY_BLUE)
    arcade.draw_xywh_rectangle_filled(0, 0, 640, 50, arcade.color.LIGHT_BROWN)
    fish.center_x = player_x
    fish.center_y = player_y
    playerlist.append(fish)
    playerlist.draw()


def on_key_press(key, modifiers):
    global up_pressed, down_pressed, right_pressed, left_pressed
    if key == arcade.key.UP:
        up_pressed = True
    if key == arcade.key.DOWN:
        down_pressed = True
    if key == arcade.key.RIGHT:
        right_pressed = True
    if key == arcade.key.LEFT:
        left_pressed = True

def on_key_release(key, modifiers):
    global up_pressed, down_pressed, right_pressed, left_pressed
    if up_pressed:
        up_pressed = False
    if down_pressed:
        down_pressed = False
    if right_pressed:
        right_pressed = False
    if left_pressed:
        left_pressed = False

    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()

import arcade
import random
import math

# global - initializing variables

WIDTH = 640
HEIGHT = 480

# player fish

player_speed = 10
player_scale = 0.1

try:
    fish = arcade.Sprite("images/fish.png", player_scale)
except:
    # image path on my computer at home
    fish = arcade.Sprite("venv/Images/fish.png", player_scale)

player_list = arcade.SpriteList()
player_list.append(fish)
fish.center_x = 100
fish.center_y = 100

# enemy fish

enemy_scale = 0.1
small_fish_count = 10
big_fish_count = 1
big_fish_list = arcade.SpriteList()
small_fish_list = arcade.SpriteList()

# scoring

score = 0
highscore = 0
final_score = 0
max = 0

# menu and buttons

current_screen = "menu"

button_height = 150
button_width = 75
button_colour = arcade.color.LIGHT_CORAL

button1 = [WIDTH / 2, HEIGHT / 2, button_height, button_width, button_colour]
button2 = [WIDTH / 2, HEIGHT / 2 - 100, button_height, button_width,
           button_colour]
button3 = [WIDTH / 2, HEIGHT / 2 + 100, button_height, button_width,
           button_colour]
menubutton = [0, HEIGHT - 35, 65, 35]

# background - ocean

background_list = arcade.SpriteList()

try:
    background = arcade.Sprite("Images/background.png", 1.95)
except:
    # image path on my computer at home
    background = arcade.Sprite("venv/Images/background.png", 1.95)

background.center_x = 320
background.center_y = 240
background_list.append(background)

# controls

up_pressed = False
down_pressed = False
right_pressed = False
left_pressed = False


# update

def update(delta_time):
    player()

    enemy_produced()

    big_fish_list.update()

    enemy_leaves()

    collision()

    resulthighscore(score)


# drawing

def on_draw():
    arcade.start_render()

    # menu screen

    if current_screen == "menu":
        global button1, button2, button3, fish_count, background

        background_list.draw()

        arcade.draw_rectangle_filled(button1[0], button1[1],
                                     button1[2], button1[3], button1[4])
        arcade.draw_text("Start", WIDTH / 2 - 30, HEIGHT / 2 - 10,
                         arcade.color.BLACK, 18)

        arcade.draw_rectangle_filled(button2[0], button2[1],
                                     button2[2], button2[3], button2[4])
        arcade.draw_text("Instructions", WIDTH / 2 - 65, HEIGHT / 2 - 110,
                         arcade.color.BLACK, 18)

        arcade.draw_rectangle_filled(button3[0], button3[1], button3[2],
                                     button3[3], button3[4])
        arcade.draw_text("High Score:", WIDTH / 2 - 65, HEIGHT / 2 + 100,
                         arcade.color.BLACK, 18)

        arcade.draw_text(f"{highscore}", WIDTH / 2 - 25, HEIGHT / 2 + 70,
                         arcade.color.BLACK, 18)

    # game screen

    if current_screen == "game":
        arcade.draw_xywh_rectangle_filled(0, 0, WIDTH, HEIGHT,
                                          arcade.color.SKY_BLUE)

        arcade.draw_xywh_rectangle_filled(0, 0, WIDTH, 50,
                                          arcade.color.LIGHT_BROWN)

        arcade.draw_xywh_rectangle_filled(menubutton[0], menubutton[1],
                                          menubutton[2], menubutton[3],
                                          arcade.color.BLACK)

        arcade.draw_text("Menu", WIDTH - 630, HEIGHT - 20,
                         arcade.color.GRAY_BLUE, 12)

        arcade.draw_text(f"Score: {score}", WIDTH - 100, HEIGHT - 20,
                         arcade.color.BLACK, 12)

        player_list.draw()

        big_fish_list.draw()
        small_fish_list.draw()

    # game over screen

    if current_screen == "GAME OVER":
        arcade.draw_xywh_rectangle_filled(0, 0, WIDTH, HEIGHT,
                                          arcade.color.SKY_BLUE)

        arcade.draw_text("GAME OVER", WIDTH / 2 - 250, HEIGHT / 2 - 30,
                         arcade.color.BLACK, 60)

        arcade.draw_xywh_rectangle_filled(0, HEIGHT - 35, 65, 35,
                                          arcade.color.BLACK)

        arcade.draw_text("Menu", WIDTH - 630, HEIGHT - 20,
                         arcade.color.GRAY_BLUE, 12)

    # instructions screen

    if current_screen == "instructions":
        background_list.draw()

        arcade.draw_xywh_rectangle_filled(0, HEIGHT - 35, 65, 35,
                                          arcade.color.BLACK)

        arcade.draw_text("Menu", WIDTH - 630, HEIGHT - 20,
                         arcade.color.GRAY_BLUE, 12)

        arcade.draw_text("Fish Eat Fish", WIDTH / 2 - 120, HEIGHT - 50,
                         arcade.color.BLACK, 30)

        arcade.draw_text("1. Use the arrow keys to move the player fish
                         up, down, left and right",
                         WIDTH / 2 - 300, HEIGHT - 100, arcade.color.BLACK, 13)
        arcade.draw_text("2. Eat fish of smaller size and increase in size",
                         WIDTH / 2 - 300, HEIGHT - 130, arcade.color.BLACK, 13)
        arcade.draw_text("3. If you try to eat fish larger than the
                         player fish, GAME OVER.", WIDTH / 2 - 300,
                         HEIGHT - 160, arcade.color.BLACK, 13)
        arcade.draw_text("4. The goal is to be the largest fish in the ocean.",
                         WIDTH / 2 - 300, HEIGHT - 190, arcade.color.BLACK, 13)
        arcade.draw_text("5. Enjoy and just keep swimming!",
                         WIDTH / 2 - 300, HEIGHT - 220, arcade.color.BLACK, 13)


# key press of arrow keys

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


# key release after arrow keys are pressed

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


# clicking of buttons

def on_mouse_press(x, y, button, modifiers):
    global current_screen, button1, button_width, button_height, menubutton

    if x > button1[0] - button_width / 2 and x < button1[0] + button_width / 2
    and y > button1[1] - button_height / 2
    and y < button1[1] + button_height / 2:
        current_screen = "game"

    if x > button2[1] - button_width / 2 and x < button2[0] + button_width / 2
    and y > button2[1] - button_height / 2
    and y < button2[1] + button_height / 2:
        current_screen = "instructions"

    if x > menubutton[0] and x < menubutton[0] + menubutton[2]
    and y > menubutton[1] and y < menubutton[1] + menubutton[3]:
        current_screen = "menu"


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


# movement and speed of player fish using arrow keys

def player():
    global down_pressed, up_pressed, player_speed, fish, score, current_screen,
    player_scale, enemy_scale

    if up_pressed:
        fish.center_y += player_speed
    if down_pressed:
        fish.center_y -= player_speed
    if right_pressed:
        fish.center_x += player_speed
    if left_pressed:
        fish.center_x -= player_speed

    if fish.center_x <= 0:
        fish.center_x = 20
    if fish.center_x >= WIDTH:
        fish.center_x = WIDTH - 20
    if fish.center_y <= 0:
        fish.center_y = 50
    if fish.center_y >= HEIGHT:
        fish.center_y = HEIGHT - 20


# enemy fish spawning

def enemy_produced():
    global enemy_scale

    try:
        enemy_fish = arcade.Sprite("images/enemyfish.png", enemy_scale)
    except:
        # image path on my computer at home
        enemy_fish = arcade.Sprite("venv/Images/enemyfish.png", enemy_scale)

    # big fish spawn

    if len(big_fish_list) < big_fish_count:

        enemy_multiply = random.randrange(15, 20)
        enemy_scale = player_scale * enemy_multiply / 10

        enemy_fish.center_x = random.randrange(0, WIDTH)
        enemy_fish.center_y = random.randrange(50, HEIGHT)
        enemy_fish.change_x = random.randrange(-2, 2)
        enemy_fish.change_y = random.randrange(-2, 2)

        # pythagereon therom to find distance from player and big fish,
        # only append if far enough

        a = enemy_fish.center_x - fish.center_x
        b = enemy_fish.center_y - fish.center_y

        dist = math.sqrt(a ** 2 + b ** 2)

        # do not spawn enemy on player

        if dist > 500:
            big_fish_list.append(enemy_fish)

    # small fish spawn

    if len(small_fish_list) < small_fish_count:
        enemy_multiply = random.randrange(4, 7)
        enemy_scale = player_scale * enemy_multiply / 10

        enemy_fish.center_x = random.randrange(0, WIDTH)
        enemy_fish.center_y = random.randrange(50, HEIGHT)
        enemy_fish.change_x = random.randrange(-2, 2)
        enemy_fish.change_y = random.randrange(-2, 2)
        small_fish_list.append(enemy_fish)


# if enemy leaves screen, destroyed

def enemy_leaves():
    for enemy_fish in big_fish_list:

        if enemy_fish.left > WIDTH or
        enemy_fish.right < 0 or
        enemy_fish.bottom > HEIGHT or
        enemy_fish.top < 0:
            enemy_fish.kill()

    for enemy_fish in small_fish_list:

        if enemy_fish.left > WIDTH or
        enemy_fish.right < 0 or
        enemy_fish.bottom > HEIGHT or
        enemy_fish.top < 0:
            enemy_fish.kill()


# collision of player and enemy ; game over with big fish, eat small fish
def collision():

    global score, current_screen, player_scale, enemy_fish, enemy

    for enemy in arcade.check_for_collision_with_list(fish, big_fish_list):
        fish.scale = player_scale
        fish.center_x = 100
        fish.center_y = 100
        current_screen = "GAME OVER"

    for enemy in arcade.check_for_collision_with_list(fish, small_fish_list):
        score += 1
        fish.width += enemy.width / 20
        fish.height += enemy.width / 20

        enemy.kill()


# score is saved to highscore

def resulthighscore(score):
    global final_score, highscore

    if current_screen == "GAME OVER":
        final_score = score

    if final_score > highscore:
        highscore = final_score


if __name__ == '__main__':
    setup()

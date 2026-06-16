import matplotlib.pyplot as plt
import numpy as np
import os
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

screen_x, screen_y = 1280, 720

# Create data for background
dat = []
for i in range(1, 10):
    dat.extend(np.repeat(i, i*2))

# Create background
dpi = 300
fontsize = 8
plt.clf()
plt.figure(figsize=(screen_x/dpi, screen_y/dpi), dpi=dpi)
plt.hist(dat, bins=np.arange(0,11,1), edgecolor='black', color='steelblue')
plt.xlim(0, 10)
plt.xticks(np.arange(0, 11, 1), fontsize = fontsize - 3)
plt.yticks(np.arange(0, 26, 5), fontsize = fontsize - 3)
plt.title("Intro to Python for Data Analysis: The Game", fontsize = fontsize)
plt.xlabel("Use the Arrow Keys to Move | Help the Analyst Install Python", fontsize = fontsize - 1.5)
plt.tight_layout()
plt.savefig("assets/game-bg.png", dpi=dpi)

# Game
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((screen_x, screen_y))
clock = pg.time.Clock()

bg = pg.image.load("assets/game-bg.png").convert()
p1 = pg.image.load("assets/player.png").convert_alpha()
py_logo = pg.image.load("assets/py-logo.png").convert_alpha()
win_img = pg.image.load("assets/win-img.png").convert_alpha()
win_sound = pg.mixer.Sound("assets/win-sound.wav")
jump_sound = pg.mixer.Sound("assets/jump.wav")

p1 = pg.transform.scale(p1, (p1.get_width() * .1, p1.get_height() * .1))
win_img = pg.transform.scale(win_img, (win_img.get_width() * .1, win_img.get_height() * .1))
py = pg.transform.scale(py_logo, (py_logo.get_width() * 1/3, py_logo.get_height() * 1/3))

p1_pos = pg.Vector2(120, 470)
py_pos = pg.Vector2(screen.get_width() - py.get_width() - 70, 125)

dt = .1 # 'delta time' - the time between each frame, in seconds
running = True
mvmt = 33 * dt
velo = 0
grav = 900
jump_pwr = -350
on_ground = True
ground = 470

while running:
    # Check for exit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Put images on screen
    screen.blit(bg, (0, 0))
    screen.blit(py, py_pos)
    screen.blit(p1, p1_pos)

    # Player + logo hitboxes
    p1_hbox = pg.Rect(p1_pos.x, p1_pos.y, p1.get_width(), p1.get_height())
    py_hbox = pg.Rect(py_pos.x, py_pos.y, py.get_width(), py.get_height())

    # Bar hitboxes
    bars = []
    bar_w, bar_h = 112, 39
    init_x, init_y = 211, 543
    for i in range(9):
        bars.append(pg.Rect(init_x + i*bar_w, init_y - i*bar_h, bar_w, (i+1)*bar_h))
    #for bar in bars:
    #    pg.draw.rect(screen, (255, 0, 0), bar)

    keys = pg.key.get_pressed() # Check for key presses
    p1_oldpos_x = p1_pos.x      # Store old x-pos

    if keys[pg.K_LEFT] and p1_pos.x - mvmt > 103:
        p1_pos.x -= mvmt
    if keys[pg.K_RIGHT] and p1_pos.x + mvmt + p1.get_width() < 1220:
        p1_pos.x += mvmt

    # Redraw hitbox after movement
    p1_hbox = pg.Rect(p1_pos.x, p1_pos.y, p1.get_width(), p1.get_height())

    # Check for horizontal collisions with bars
    for bar in bars:
        if p1_hbox.colliderect(bar) and p1_hbox.bottom > bar.top + 2:
            p1_pos.x = p1_oldpos_x
            break

    if keys[pg.K_UP] and on_ground:
        velo = jump_pwr
        on_ground = False
        jump_sound.play()

    old_bottom = p1_pos.y + p1.get_height()

    velo += grav * dt
    p1_pos.y += velo * dt

    # Redraw hitbox after movement
    p1_hbox = pg.Rect(p1_pos.x, p1_pos.y, p1.get_width(), p1.get_height())

    on_ground = False

    for bar in bars:
        crossed_bar_top = old_bottom <= bar.top and p1_hbox.bottom >= bar.top
        overlaps_bar_x = p1_hbox.right > bar.left and p1_hbox.left < bar.right
        if velo >= 0 and crossed_bar_top and overlaps_bar_x:
            p1_pos.y = bar.top - p1.get_height()
            velo = 0
            on_ground = True
            break
            
    if p1_pos.y >= ground:
        p1_pos.y = ground
        velo = 0
        on_ground = True

    # Flip frame
    pg.display.flip()

    # Play sound, change player image, etc. when player reaches logo
    if p1_hbox.colliderect(py_hbox):
        screen.blit(bg, (0, 0))
        screen.blit(win_img, (py_pos.x, py_pos.y - 10))
        pg.display.flip()
        win_sound.play()
        pg.time.wait(5000)
        running = False
    
    dt = clock.tick(60) / 1000
    dt = max(0.001, min(0.1, dt))

pg.quit()
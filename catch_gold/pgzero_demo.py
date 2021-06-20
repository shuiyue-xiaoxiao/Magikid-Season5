import pgzrun

WIDTH, HEIGHT = 600, 600
gold_x, gold_y = 300, 30
vel_y = 10

def draw():
    screen.fill("black")
    screen.draw.filled_circle((gold_x, gold_y), 30, "yellow")

def update():
    global gold_x, gold_y, vel_y
    gold_y += vel_y
    if gold_y <= 0 + 30 or gold_y >= HEIGHT - 30:
        vel_y = - vel_y

pgzrun.go()

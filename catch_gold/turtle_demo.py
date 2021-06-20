from turtle import *
import time

WIDTH, HEIGHT = 600, 600
setup(WIDTH, HEIGHT)
bgcolor("black")
title("Catch Gold")

def gold():
    color("yellow")
    dot(50)

def pen_goto(a, b):
    up()
    goto(a, b)
    down()

a, b = 0, 275
def drop_down():
    global a, b
    for i in range(55):
        tracer(0)
        clear()
        pen_goto(a, b)
        gold()
        b -= 10
        update()
        time.sleep(0.01)

def drop_up():
    global a, b
    for i in range(55):
        tracer(0)
        clear()
        pen_goto(a, b)
        gold()
        b += 10
        update()
        time.sleep(0.01)

try:
    while True:
        drop_down()
        drop_up()
except:
    print("Exit")

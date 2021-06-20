from turtle import *
import time

w, h = 600, 800
setup(w, h)
bgcolor("blue")
title("ball")


def pen_goto(x, y):
    penup()
    goto(x, y)
    pendown()


def ball():
    dot(50, "yellow")


a, b = 0, 375


def down():
    global a, b
    for i in range(75):
        tracer(0)
        clear()
        pen_goto(a, b)
        ball()
        b -= 10
        update()
        time.sleep(0.01)


def up():
    global a, b
    for j in range(75):
        tracer(0)
        clear()
        pen_goto(a, b)
        ball()
        b += 10
        update()
        time.sleep(0.01)


hideturtle()

while True:
    down()
    up()

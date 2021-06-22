from turtle import *
import time

hideturtle()
w, h = 600, 800
setup(w, h)
bgcolor("blue")
title("ball")


def pen_goto(x, y):
    penup()
    goto(x, y)
    pendown()


def t():
    dot(50, "black")


def _t():
    dot(50, "black")


x, y = 0, 375
_x, _y = 275, 0


def _down():
    global x, y
    for i in range(75):
        tracer(0)
        clear()
        pen_goto(x, y)
        _t()
        y -= 10
        update()
        time.sleep(0.01)


def _up():
    global x, y
    for j in range(75):
        tracer(0)
        clear()
        pen_goto(x, y)
        _t()
        y += 10
        update()
        time.sleep(0.01)


def _left():
    global _x, _y
    for i in range(55):
        tracer(0)
        clear()
        pen_goto(_x, _y)
        t()
        _x -= 10
        update()
        time.sleep(0.01)


def _right():
    global _x, _y
    for j in range(55):
        tracer(0)
        clear()
        pen_goto(_x, _y)
        t()
        _x += 10
        update()
        time.sleep(0.01)


while True:
    _down()
    _up()
    _left()
    _right()


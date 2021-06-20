from tkinter import *
import time

window = Tk()
window.title("Catch Gold")

WIDTH, HEIGHT = 600, 600
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

gold = canvas.create_oval((275, 0), (325, 50), fill="yellow")

# 动画
gold_x, gold_y = 0, 10
try:
    while True:
        canvas.move(gold, gold_x, gold_y)
        pos = canvas.coords(gold)  # [x1, y1, x2, y2]
        if pos[1] <= 0 or pos[3] >= HEIGHT:
            gold_y = -gold_y
        window.update()
        time.sleep(0.01)
except:
    print("Exit")

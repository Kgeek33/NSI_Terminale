# alias de l’import turtle : t
import turtle as t
from time import sleep
from random import choice

colors = ["blue", "white", "yellow", "red", "pink", "purple"]


def segment_vk(lg, n_p):
    if n_p == 0:
        t.color(choice(colors))
        t.forward(lg)
    else:
        segment_vk(lg / 3, n_p - 1)
        t.left(60)
        segment_vk(lg / 3, n_p - 1)
        t.right(120)
        segment_vk(lg / 3, n_p - 1)
        t.left(60)
        segment_vk(lg / 3, n_p - 1)


def flocon(fois):
    for _ in range(3):
        segment_vk(650, fois)
        t.right(120)


t.penup()
t.bgcolor("black")
t.goto(-350, 200)
t.pendown()
t.speed(0)
t.pensize(3)

flocon(4)
sleep(2.5)

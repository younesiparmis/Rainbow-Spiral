from turtle import *
import random

speed(0)
bgcolor("black")

colors = ["red", "yellow", "cyan", "magenta", "lime"]

for i in range(120):
    color(random.choice(colors))
    pensize(2)
    forward(i * 2)
    left(119)

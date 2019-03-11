# -*- coding: utf-8 -*-
from tsp import Tsp
import tkinter

SCREEN_WIDTH = 360
SCREEN_HEIGHT = 360

tsp = Tsp(
    gene_size=50,
    item_size=20,
    selection_rate=0.5,
    mutation_rate=0.3,
)

for i in range(0, 1000):
    tsp.cycle()
    print(str(tsp.generation) + 'G')

root = tkinter.Tk()
root.title('GA TSP: ' + str(tsp.generation) + 'G')
root.geometry(str(SCREEN_WIDTH) + 'x' + str(SCREEN_HEIGHT))
canvas = tkinter.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.place(x=0, y=0)

canvas.delete('all')

item = tsp.top()
distance = tsp.evaluate(item)

for start in range(len(item)):
    end = start + 1
    if end == len(item):
        end = 0
    p1 = tsp.points[item[start]]
    p2 = tsp.points[item[end]]
    canvas.create_line(
        p1.x * SCREEN_WIDTH,
        p1.y * SCREEN_HEIGHT,
        p2.x * SCREEN_WIDTH,
        p2.y * SCREEN_HEIGHT,
        fill='blue',
        width=1
    )
    canvas.create_oval(
        p1.x * SCREEN_WIDTH - 3,
        p1.y * SCREEN_HEIGHT - 3,
        p1.x * SCREEN_WIDTH + 3,
        p1.y * SCREEN_HEIGHT + 3,
        fill='green'
    )

canvas.create_text(
    5, 5,
    text="{:.2f}".format(distance),
    anchor='nw',
    fill='red'
)
canvas.update()

root.mainloop()

from PIL import ImageTk, Image
from tkinter import *

def _create_circle(canvas, pos, r, **kwargs):
	x, y = (pos[0] * 2, pos[1] * 2)
	canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)

def _create_line(canvas, pos1, pos2, **kwargs):
	x1, y1 = (pos1[0] * 2, pos1[1] * 2)
	x2, y2 = (pos2[0] * 2, pos2[1] * 2)
	canvas.create_line(x1, y1, x2, y2, width = 2.5, arrow=LAST, **kwargs)
from PIL import ImageTk, Image
from tkinter import *

def _create_circle(canvas, x, y, r, **kwargs):
	canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

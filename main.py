import tkinter as tk
import tkinter.ttk as ttk
import ttkthemes
import time
from tkinter import *
from PIL import ImageTk, Image

#private modules
from src.colors import monokai

from src.instances.victim import AliveVictim, DeadVictim
from src.instances.points import Point, Line
from src.instances.rescueInfos import RescueInfo
from src.pipeline import Pipeline
#



class App(tk.Frame):
	def __init__(self, root = None):
		super().__init__(root)
		self.root = root
		self.process = True
		self.drawList = []

		self.root.geometry("600x622")
		self.pack()

		self.canvas = Canvas(root, width = 600, height = 622)
		self.canvas.pack()

		self.rescue_img = ImageTk.PhotoImage(Image.open("./res/rescue.png"))
		self.pipeline = Pipeline("./res/out.txt")

		menubar = Menu(self.master)
		self.root.config(menu=menubar)
		debugMenu = Menu(menubar)
		debugMenu.add_command(label="fuk edu", command=self.debug)
		menubar.add_cascade(label="Debug", menu=debugMenu)

	def debug(self):
		print("fuk edu")

	def quit(self):
		self.process = False

	def create_rescue(self):
		self.canvas.create_image(0, 0, anchor=NW, image=self.rescue_img)

	def mainloop(self):
		self.root.protocol("WM_DELETE_WINDOW", self.quit)
		#self.drawList.append(AliveVictim((100, 150)))
		#self.drawList.append(DeadVictim((150, 100)))
		#self.drawList.append(Point((150, 150), monokai["red"]))
		#self.drawList.append(Line((10, 10), (50, 50), monokai["blue"]))

		while self.process:
			self.canvas.delete("all")

			self.create_rescue()

			for entity in self.drawList:
				if(entity.deleteQuery):
					self.drawList.remove(entity)
				else:
					if(entity is not None):
						try:
							entity.draw(self.canvas)
						except Exception as e:
							print("Error on draw entity, e:", e)
					else:
						print("Entity not found")
						del entity

			time.sleep(0.32)
			self.root.update()

root = tk.Tk()
root.iconphoto(False, PhotoImage(file = './res/logo.png'))
root.resizable(False, False)

ttkthemes.themed_style.ThemedStyle(theme="breeze")

app = App(root)
app.mainloop()
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
from src.pipeline import Pipeline, Parser
#

class App(tk.Frame):
	def __init__(self, root = None):
		super().__init__(root)
		self.root = root
		self.process = True
		self.drawIdentifiedList = [None] * 255
		self.drawFreeList = []

		self.canvas = Canvas(root, width = 600, height = 622)
		self.canvas.pack()

		self.rescue_img = ImageTk.PhotoImage(Image.open("./res/rescue.png"))
		self.rescue = RescueInfo()
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

	def update(self, line):
		res = Parser.check(line)

		if res[0] == "ALIVEVICTIM" or res[0] == "DEADVICTIM":
			self.drawIdentifiedList[res[2]] = res[1]
		elif res[0] == "POINT" or res[0] == "LINE":
			self.drawFreeList.append(res[1])
		elif res[0] == "RESCUE":
			self.rescue.triangle = res[1]["triangle"]
			self.rescue.exit = res[1]["exit"]
		elif res[0] == "CLEARLINES":
			self.drawFreeList = []


	def mainloop(self):
		self.root.protocol("WM_DELETE_WINDOW", self.quit)

		while self.process:
			#Read infos process
			self.pipeline.update(self.update)

			#Render process
			self.canvas.delete("all")

			self.create_rescue()

			for entity in self.drawIdentifiedList:
				if(entity is not None):
					if(entity.deleteQuery):
						self.drawIdentifiedList.remove(entity)
					else:
						try:
							entity.draw(self.canvas)
						except Exception as e:
							print("Error on draw identified entity, e:", e)

			for entity in self.drawFreeList:
				if(entity is not None):
					if(entity.deleteQuery):
						self.drawFreeList.remove(entity)
					else:
						try:
							entity.draw(self.canvas)
						except Exception as e:
							print("Error on draw free entity, e:", e)

			time.sleep(0.32)
			self.root.update()

root = tk.Tk()
root.title("sBotics viewer")
root.geometry("600x622")
root.resizable(False, False)
root.iconphoto(False, PhotoImage(file = './res/logo.png'))
ttkthemes.themed_style.ThemedStyle(theme="breeze")

app = App(root)
app.mainloop()
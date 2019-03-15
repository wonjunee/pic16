"""
tk_square.py
"""

# import Tkinter as Tk #or tkinter in v.3
# root = Tk.Tk()
# w = Tk.Canvas(root, width=500, height=500)
# w.pack()
# def rectangle(event):
#     w.create_rectangle(event.x,event.y, event.x+20, event.y+20, fill="blue")
# w.bind("<Button-1>", rectangle)
# root.mainloop()
import random 

import Tkinter as Tk #or tkinter in v.3
class RectangleGUI:
	def __init__(self, master):
		self.master = master
		self.c = 50
		self.colors = ["red", "orange", "yellow", "green", "blue", "violet"]
		self.d = 200
		self.x = 50
		self.y = 50
		self.canvas = Tk.Canvas(master, width=400, height=400)
		self.canvas.create_rectangle(self.x, self.y, self.x+self.d, self.y+self.d, fill="blue")
		self.canvas.pack()
		self.canvas.bind('<Button-1>', self.change_color)
	def change_color(self,ev):
		if (ev.x < self.x+self.d) & (ev.x > self.x) & (ev.y < self.y+self.d) & (ev.y > self.y):
			self.canvas.create_rectangle(self.x, self.y, self.x+self.d, self.y+self.d, fill=random.choice(self.colors))
		else:
			print "NONONO"

root = Tk.Tk()
gui=RectangleGUI(root)
root.mainloop()
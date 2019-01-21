# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 19:46:59
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-09 20:37:29

import tkinter as tk

def scale_function(value):
	print(value)

def show_scale(label, scale):
	print(scale.get())
	label.config(text="Your selection is {}".format(scale.get()))

if __name__ == '__main__':
	# window body
	root = tk.Tk()
	root.title("scale")
	root.geometry("200x200")

	# label
	label_demo = tk.Label(
		root,
		width=15,
		height=2,
		bg="yellow",
		font=("Arial",12),
		text="empty"
	)
	label_demo.pack()

	# scale
	scale_demo = tk.Scale(
		root,
		length=200,
		label="Old Scale",
		from_=0,
		to=100,
		orient=tk.HORIZONTAL,
		showvalue=1,
		tickinterval=10,
		resolution=1,
		command=scale_function
	)
	scale_demo.pack()

	# button
	button_demo = tk.Button(
		root,
		width=10,
		height=1,
		font=("Arial",12),
		text="get scale",
		command=lambda:show_scale(label_demo, scale_demo)
	)
	button_demo.pack()

	# mainloop
	root.mainloop()
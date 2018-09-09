# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 20:39:03
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-09 20:43:28

import tkinter as tk

def cheakbutton_function(value):
	print(value)

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

	# cheakbutton
	cheakbutton_demo = tk.Cheakbutton(
		root,
		width=10,
		height=1,
		font=("Arial",12),
		text="get scale",
		command=lambda:show_scale(label_demo, scale_demo)
	)
	cheakbutton_demo.pack()

	# mainloop
	root.mainloop()
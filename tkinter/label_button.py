# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-08 11:36:00
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-08 12:32:41

import tkinter as tk

def button_function(string_var):
	string_var.set(string_var.get()+"*")

if __name__ == '__main__':
	# window body
	root = tk.Tk()
	root.title("label_button")
	root.geometry("200x200")

	# label
	string = tk.StringVar()
	label_demo = tk.Label(
		root,
		width=15,
		height=2,
		bg="green",
		font=("Arial",12),
		textvariable=string
	)
	label_demo.pack()

	# button
	button_demo = tk.Button(
		root,
		width=15,
		height=2,
		text="hit me",
		bg="red",
		font=("Arial",12),
		command=lambda:button_function(string)
	)
	button_demo.pack()

	# mainloop
	root.mainloop()

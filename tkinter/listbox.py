# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-08 22:13:01
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-11 00:00:04

import tkinter as tk

def button_function(listbox, string_var):
	try:
		value = listbox.get(listbox.curselection())
		index, = listbox.curselection()
		print(index)
	except:
		value = "No"
	string_var.set(value)

if __name__ == '__main__':
	# window body
	root = tk.Tk()
	root.title("listbox")
	root.geometry("200x200")

	# label
	label_string = tk.StringVar()
	label_demo = tk.Label(
		root,
		width=15,
		height=2,
		bg="yellow",
		font=("Arial",12),
		textvariable=label_string
	)
	label_demo.pack()

	# button
	button_demo = tk.Button(
		root,
		width=15,
		height=1,
		text="print selection",
		# bg="red",
		font=("Arial",12),
		command=lambda:button_function(listbox_demo, label_string)
	)
	button_demo.pack()

	# listbox
	listbox_demo = tk.Listbox(
		root,
		width=10,
		height=1,
		# bg="red",
		font=("Arial",12),
		# listvariable=listbox_string
	)
	listbox_items = list(range(100))
	for item in listbox_items:
		listbox_demo.insert('end', item)
	listbox_demo.insert(1, "yes")
	listbox_demo.insert(2, "no")
	listbox_demo.delete(2)
	listbox_demo.pack()

	# mainloop
	root.mainloop()
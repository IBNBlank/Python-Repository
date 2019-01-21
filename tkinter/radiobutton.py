# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 18:58:06
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-09 20:00:26

import tkinter as tk

def radiobutton_function(label, string):
	label.config(text="Your selection is {}".format(string.get()))

if __name__ == '__main__':
	# window body
	root = tk.Tk()
	root.title("radiobutton")
	root.geometry("200x200")

	# label
	string = tk.StringVar()
	label_demo = tk.Label(
		root,
		width=15,
		height=2,
		bg="yellow",
		font=("Arial",12),
		text="empty"
	)
	label_demo.pack()

	# radiobutton
	string = tk.StringVar()
	radiobutton_demo_1 = tk.Radiobutton(
		root,
		width=15,
		height=1,
		text="Option_A",
		font=("Arial",12),
		variable=string,
		value="A",
		command=lambda:radiobutton_function(label_demo, string)
	)
	radiobutton_demo_1.pack()
	radiobutton_demo_2 = tk.Radiobutton(
		root,
		width=15,
		height=1,
		text="Option_B",
		font=("Arial",12),
		variable=string,
		value="B",
		command=lambda:radiobutton_function(label_demo, string)
	)
	radiobutton_demo_2.pack()
	radiobutton_demo_3 = tk.Radiobutton(
		root,
		width=15,
		height=1,
		text="Option_C",
		font=("Arial",12),
		variable=string,
		value="C",
		command=lambda:radiobutton_function(label_demo, string)
	)
	radiobutton_demo_3.pack()

	# mainloop
	root.mainloop()
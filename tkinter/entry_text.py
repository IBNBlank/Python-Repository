# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-08 12:23:06
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-08 22:29:20

import tkinter as tk

def insert_start_function(entry, text):
	string = entry.get()
	text.insert(1.0, string)

def insert_point_function(entry, text):
	string = entry.get()
	text.insert("insert", string)

def insert_end_function(entry, text):
	string = entry.get()
	text.insert("end", string)

if __name__ == '__main__':
	# window body
	root = tk.Tk()
	root.title("test")
	root.geometry("200x200")

	# entry
	entry_demo = tk.Entry(
		root,
		width=15,
		bg="red",
		font=("Arial",12),
		show="*"
	)
	entry_demo.pack()

	# button
	insert_start = tk.Button(
		root,
		width=15,
		height=1,
		text="insert start",
		font=("Arial",12),
		command=lambda:insert_start_function(entry_demo, text_demo)
	)
	insert_start.pack()
	insert_point = tk.Button(
		root,
		width=15,
		height=1,
		text="insert point",
		font=("Arial",12),
		command=lambda:insert_point_function(entry_demo, text_demo)
	)
	insert_point.pack()
	insert_end = tk.Button(
		root,
		width=15,
		height=1,
		text="insert end",
		font=("Arial",12),
		command=lambda:insert_end_function(entry_demo, text_demo)
	)
	insert_end.pack()

	# text
	text_demo = tk.Text(
		root,
		width=15,
		height=3,
		font=("Arial",12)
	)
	text_demo.pack()

	# mainloop
	root.mainloop()
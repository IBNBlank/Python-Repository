# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 20:39:03
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-10 23:10:31

import tkinter as tk

def checkbutton_function(var1, var2, label):
    if (var1.get() == 1) & (var2.get() == 0):
        label.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        label.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        label.config(text='I do not love either')
    else:
        label.config(text='I love both')

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
		text="unknown"
	)
	label_demo.pack()

	# checkbutton
	check_var_1 = tk.IntVar()
	check_var_2 = tk.IntVar()
	checkbutton_demo_1 = tk.Checkbutton(
		root,
		width=10,
		height=1,
		font=("Arial",12),
		text="Python",
		variable=check_var_1,
		onvalue=1,
		offvalue=0,
		command=lambda:checkbutton_function(check_var_1, check_var_2, label_demo)
	)
	checkbutton_demo_1.pack()
	checkbutton_demo_2 = tk.Checkbutton(
		root,
		width=10,
		height=1,
		font=("Arial",12),
		text="C++",
		variable=check_var_2,
		onvalue=1,
		offvalue=0,
		command=lambda:checkbutton_function(check_var_1, check_var_2, label_demo)
	)
	checkbutton_demo_2.pack()

	# mainloop
	root.mainloop()
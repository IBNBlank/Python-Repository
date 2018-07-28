# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-02-11 19:55:07
# @Last Modified by:   Administrator
# @Last Modified time: 2018-02-11 21:35:48
message = input("Please enter cmd")

if message == "Dong":
	print("Last Name")
elif message == "Zhaorui":
	print("First Name")
else:
	print("输入错误")

if (not message == "Dong") and (not message == "Zhaorui"):
	print("Not right message")
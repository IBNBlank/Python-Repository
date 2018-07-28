# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-02-13 19:55:00
# @Last Modified by:   Administrator
# @Last Modified time: 2018-02-13 21:13:56

# 变量单词间用下划线
# 类用驼峰命名法

class WowDog():
	def __init__(self,user_input_name):
		self.name = user_input_name
		self.x = 0
	def move(self):
		self.x += 10
	def say_name(self):
		print("My name is {}".format(self.name))
	def bark(self):
		print("Wow! Wow!")

yellow = WowDog("Da Huang")
white  = WowDog("Xiao Bai")

yellow.say_name()
yellow.bark()

white.say_name()
white.bark()
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-03-01 20:25:49
# @Last Modified by:   Administrator
# @Last Modified time: 2018-03-03 01:11:43
import json

with open("my_data.json","r") as load_f:
	data = json.load(load_f)
	print("{0} is {1}. The age is {2}".format(data["name"],data["gender"],data["age"]))
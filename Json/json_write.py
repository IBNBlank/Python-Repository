# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-03-01 20:26:27
# @Last Modified by:   Administrator
# @Last Modified time: 2018-03-03 01:07:39
import json

with open("my_data.json","w") as load_f:
	data = {
		"name":"Lilei",
		"gender":"Male",
		"age":26
	}
	json.dump(data, load_f)
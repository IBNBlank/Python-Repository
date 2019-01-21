# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-03-01 20:26:27
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-09 00:05:40
import json

with open("my_data.json","w") as load_f:
	data = {
		"name":["Lilei","haha"],
		"gender":"Male",
		"age":26
	}
	json.dump(data, load_f)
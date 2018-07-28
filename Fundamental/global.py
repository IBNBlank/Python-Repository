# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-07-21 17:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-07-28 23:56:44

a = 10

def test_1():
	a = 1

def test_2():
	global a
	a = 1

if __name__ == '__main__':
	test_1()
	print(a)

	test_2()
	print(a)
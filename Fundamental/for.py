# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-02-11 21:03:29
# @Last Modified by:   Administrator
# @Last Modified time: 2018-02-11 21:28:34
student_list = ["student1","student2","student3","student4"]

for student in student_list:
	print(student)

print("*"*60)

for i in range(0,4,2):
	print(i)
	print(student_list[i])

print("*"*60)

for i in range(10): #range(10)相当于range(0,10,1)
	print(i)
	if i > 5:
		break

print("*"*60)

i = 0
while True:
	print(i)
	i = i + 1
	if i > 5:
		break

print("*"*60)

for i in range(10): #range(10)相当于range(0,10,1)
	if i == 5:
		continue
	print(i)

print("*"*60)
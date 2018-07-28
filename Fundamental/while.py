# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-02-11 19:55:30
# @Last Modified by:   Administrator
# @Last Modified time: 2018-02-13 20:48:55
i = 1
while i < 10:
	print(i)
	i += 1	#i++不行

user_input_sex_correct = False
user_input_sex = input("Sex(F/M)\n")
while not user_input_sex_correct:
	if user_input_sex == "F":
		print("性别为女")
		user_input_sex_correct = True
	elif user_input_sex == "M":
		print("性别为男")
		user_input_sex_correct = True
	else:
		user_input_sex = input("Wrong input(F/M)\n")

user_input_age_correct = False
user_input_age = input("Age(digit)\n")
user_input_age_correct = user_input_age.isdigit()
while not user_input_age_correct:
	user_input_age = input("Wrong input(digit)\n")
	user_input_age_correct = user_input_age.isdigit()
print("Age is",user_input_age)


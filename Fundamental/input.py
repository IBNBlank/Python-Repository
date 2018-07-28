# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-02-09 21:54:44
# @Last Modified by:   Administrator
# @Last Modified time: 2018-02-09 23:14:22
import time

name   = input("Please enter your name  :")
sex    = input("Please enter your sex   :")
age    = input("Please enter your age   :")
school = input("Please enter your school:")

resume = {"name":name,"sex":sex,"age":age,"school":school}

print("\nResume is being generated",end='')
time.sleep(0.5)
print("\rResume is being generated.",end='')
time.sleep(0.5)
print("\rResume is being generated..",end='')
time.sleep(0.5)
print("\rResume is being generated...\n")
time.sleep(1)

print("********************************************")
print("*******************RESUME*******************")
print("********************************************\n")

print("  Name:",resume["name"])
print("   Sex:",resume["sex"])
print("   Age:",resume["age"])
print("School:",resume["school"])
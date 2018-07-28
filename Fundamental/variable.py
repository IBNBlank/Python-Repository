# Numbers:int、float、bool、complex
INT     = 1 	 #整形
FLOAT   = 1.0    #浮点型
BOOL    = True   #布尔型
COMPLEX = 1+1j   #复数

# String
String = "University" #字符串

# List
List = ["lilei","hanmeimei",98,[1,"University"],1+1j] #列表

# Dictionaries
Dictionaries = {"lilei":98,"hanmeimei":95,"madongmei":95} #字典

# Tuple
Tuple = ("lilei","hanmeimei",98,[1,"University"]) #元组（类似于列表，但不能修改）只有1个元素的Tuple定义时必须加一个逗号

# Sets
Sets_A = {10,20,30,40,50} #集合（可做加减）
Sets_B = {10,20,30} 	  #集合

print("\n数据")
print(INT,FLOAT,BOOL,COMPLEX)

print("\n字符串")
print(String)
print(String[0])
print(String[1:4]) # 表示String[1]到String[4-1]

print("\n列表")
print(List)
print(List[0])
print(List[1:4])

print("\n字典")
print(Dictionaries)
print(Dictionaries["lilei"])

print("\n元组")
print(Tuple)

print("\n集合")
print(Sets_A)
print(Sets_A-Sets_B)

##############################
## list example 1
##############################
grade = [98,99,95,80,'test']
print(grade[0]+grade[3])

# list删除
print(grade)
del grade[4]
print(grade)

##############################
## list example 2
##############################
inventory = ['钥匙','毒药']
print(inventory)

if '解药' in inventory:
	print("Yes")
else:
	print("No")

# list 添加
inventory.append('解药')
print(inventory)

if '解药' in inventory:
	print("Yes")
else:
	print("No")

##############################
## dictionaries example
##############################
student = {"李雷":98,"韩梅梅":100,"马冬梅":80}
print(student["李雷"])
print(student["韩梅梅"])

# dictionaries 删除
print(student)
del student["马冬梅"]
print(student)

# dictionaries 添加
print(student)
student["马冬梅"] = 90
print(student)
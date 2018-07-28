string_1 = 'abc'
string_2 = "abc"

#单引号双引号等价，如果文本中有单引号则用双引号，有双引号则用单引号（也可以用“\”来辅助显示）
string_3 = 'Mike said "abc"'
string_4 = "I'm abc"
string_5 = "Mike said \"abc\""
string_6 = 'I\'m abc'

#三引号用于多行
string_7 = '''\nMike
said
abc\n'''
string_8 = """\nMike
said
abc\n"""

print(string_1)
print(string_2)
print(string_3)
print(string_4)
print(string_5)
print(string_6)
print(string_7)
print(string_8)

#字符串可以当做数组来使用
print(string_1[len(string_1)-1]) #len()用来获得长度
print(string_1+string_2)
print(string_1,string_2)

#format()函数的的三种使用
#用法1
s = "I said: {} {} !".format("hello","world")
print(s)
s = "My name is: {}".format(string_1)
print(s)
#用法2
s = "I said: {1} {0} {1} !".format("hello","world")
print(s)
#用法3
s = "string_1 is: {str1}\nstring_2 is: {str2}".format(str1=string_1,str2=string_2)
print(s)

#常用字符函数
#find()函数
print("find b",string_1.find("b"))
print("find d",string_1.find("d"))
#lower()函数和upper()函数
print("lower",string_1.lower())
print("upper",string_1.upper())
#split()函数
print("split by b",string_1.split("b"))
#replace()函数
print("replace a",string_1.replace("a","hacker"))

# creat object
# bytes object
b = b"example"
# str object
s = "example"

# method one
# str to bytes
bytes(s, encoding = "utf8")
# bytes to str
str(b, encoding = "utf-8")

# method two
# str to bytes
str.encode(s)
# bytes to str
bytes.decode(b)
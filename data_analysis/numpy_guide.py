# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-22 21:13:37
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-22 23:43:45

import numpy as np

##### 创建 ndarray 类型数组 #####
### 列表创建 ###
# 一维
ndarray_1 = np.array([1, 2, 3, 4, 5])
python_list = [1, 2, 3, 4, 5]
ndarray_2 = np.array(python_list)
print(ndarray_1)
print(ndarray_2)
# 二维
ndarray_3 = np.array([[1,2,3], [4,5,6]])
ndarray_4 = np.array(
	[
		[1, 2, 3],
		[4, 5, 6]
	])
print(ndarray_3)
print(ndarray_4)
### 自带函数创建 ###
# 全零数组
ndarray_5 = np.zeros(10)
ndarray_6 = np.zeros((10,10))
print(ndarray_5)
print(ndarray_6)
# 全一数组
ndarray_7 = np.ones(10)
ndarray_8 = np.ones((10,10))
print(ndarray_7)
print(ndarray_8)
# 索引数组
ndarray_9 = np.arange(10)
print(ndarray_9)

##### 了解 ndarray 各维度的长度 #####
print(ndarray_1.shape)
print(ndarray_3.shape)

##### 输出 ndarray 特定元素 #####
### 单个 ###
print(ndarray_9[0])
print(ndarray_3[0][1])
print(ndarray_3[0,1])
### 切片 ###
print(ndarray_9[0:5])
print(ndarray_3[0, 0:2])
print(ndarray_3[:, 0])
# 对切片的所有操作都会对原始数据产生影响
temp = ndarray_9[3:6]
temp[2] *= 10
print(ndarray_9)
# 若要无影响，则需要先复制
temp = ndarray_9[3:6].copy()
temp[2] *= 10
print(ndarray_9)

##### 数组维度变化 #####
ndarray_9 = np.arange(10)
print(ndarray_9.reshape((2,5)))
print(ndarray_9.reshape((2,5)).T)

##### 对数组里每个数据进行运算 #####
ndarray_9 = np.arange(10)
ndarray_10 = np.array([1, -1, 2, -3, 4, -5, 6, -7, 8, -9])
ndarray_11 = np.sqrt(ndarray_9)
ndarray_12 = np.array([0, -1, 2, -3, 4, -5, 6, -7, 8, np.nan])
### 绝对值 ###
print(np.abs(ndarray_10))
### 平方根 ###
print(np.sqrt(ndarray_9))
### 平方 ###
print(np.square(ndarray_9))
### 计算指数 ###
print(np.exp(ndarray_10))
### 计算正负号 ###
print(np.sign(ndarray_10))
### 计算大于等于该元素的最小整数 ###
print(np.ceil(ndarray_11))
### 计算小于等于该元素的最大整数 ###
print(np.floor(ndarray_11))
### 判断非数字 ###
print(np.isnan(ndarray_12))
### 相加 ###
print(ndarray_9 + ndarray_10)
print(np.add(ndarray_9, ndarray_10))
### 相减 ###
print(ndarray_9 - ndarray_10)
print(np.subtract(ndarray_9, ndarray_10))
### 相乘 ###
print(ndarray_9 * ndarray_10)
print(np.multiply(ndarray_9, ndarray_10))
### 相除 ###
print(ndarray_9 / ndarray_10)
print(np.divide(ndarray_9, ndarray_10))
### 指数 ###
print(np.power(ndarray_10, ndarray_9))
### 计算各位置哪个更大 ###
print(np.fmax(ndarray_9, ndarray_10))
### 计算各位置哪个更小 ###
print(np.fmin(ndarray_9, ndarray_10))

##### 统计学方法 #####
### 求和 ###
print(np.sum(ndarray_9))
print(ndarray_9.sum())
### 求平均值 ###
print(np.mean(ndarray_9))
print(ndarray_9.mean())
### 标准差 ###
print(np.std(ndarray_9))
print(ndarray_9.std())
### 最大最小值 ###
print(np.min(ndarray_9))
print(ndarray_9.min())
print(np.max(ndarray_9))
print(ndarray_9.max())
### 最大最小值位置 ###
print(np.argmin(ndarray_9))
print(ndarray_9.argmin())
print(np.argmax(ndarray_9))
print(ndarray_9.argmax())
### 排序 ###
ndarray_13 = np.random.random(10)
print(ndarray_13)
ndarray_13.sort()
print(ndarray_13)

##### 读取外部文件 #####
data = np.genfromtxt("data.txt", delimiter=",")
print(data.astype(int))
print(data)
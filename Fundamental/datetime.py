# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-02-13 20:26:27
# @Last Modified by:   Administrator
# @Last Modified time: 2018-02-13 22:34:45
import datetime

########################################################
### datetime 模块 #######################################
########################################################
# datetime.date       ## 表示日期的类
# datetime.datetime   ## 表示日期时间的类
# datetime.time       ## 表示时间的类
# datetime.timedelta  ## 表示时间间隔，即两个时间点的间隔
# datetime.tzinfo     ## 时区的相关信息
########################################################

## 返回当前系统的时间
str1 = datetime.datetime.now()
print(str1)

## 返回当前日期时间的日期部分
str2 = datetime.datetime.now().date()
print(str2)

## 返回当前日期时间的时间部分
str3 = datetime.datetime.now().time()
print(str3)

## 计算时间间隔
time1 = datetime.datetime(2016,10,1)
time2 = datetime.datetime(2018,2,13)
print(time2 - time1)
print((time2 - time1).total_seconds())

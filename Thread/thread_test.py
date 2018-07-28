# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-07-21 22:36:30
# @Last Modified by:   Administrator
# @Last Modified time: 2018-07-22 08:10:09
import threading
import time

def T1_thread_job():
	print("T1 thread start.")
	time.sleep(1)
	print("T1 thread finish.")

def T2_thread_job():
	global T1_thread
	print("T2 thread start.")
	time.sleep(0.5)
	T1_thread.join()					# 等待 T1_thread 结束
	print("T2 thread finish.")

if __name__ == '__main__':
	T1_thread = threading.Thread(target=T1_thread_job)
	T1_thread.start()

	T2_thread = threading.Thread(target=T2_thread_job)
	T2_thread.start()

	print(threading.active_count())		# 激活的线程数
	print(threading.enumerate())		# 正在运行的线程的list
	print(threading.current_thread())	# 当前的线程变量

	T1_thread.join()					# 等待 T1_thread 结束
	print("all done")
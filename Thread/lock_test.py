# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-07-21 23:40:47
# @Last Modified by:   Administrator
# @Last Modified time: 2018-07-22 00:21:56
import threading

def T1_thread_job():
	global data, lock
	lock.acquire()
	for i in range(1000):
		data += 1
		print("job_1:{}".format(data))
	lock.release()

def T2_thread_job():
	global data, lock
	lock.acquire()
	for i in range(1000):
		data += 10
		print("job_2:{}".format(data))
	lock.release()

if __name__ == '__main__':
	lock = threading.Lock()
	data = 0
	T1 = threading.Thread(target=T1_thread_job)
	T2 = threading.Thread(target=T2_thread_job)
	T1.start()
	T2.start()
	T1.join()
	T2.join()
	print('all down')
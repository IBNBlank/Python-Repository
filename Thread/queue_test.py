# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-07-21 23:16:19
# @Last Modified by:   Administrator
# @Last Modified time: 2018-07-21 23:38:32
import threading
import time
from queue import Queue

def thread_job(l, q):
	for i in range(len(l)):
		l[i] **= 2
	q.put(l)

def multi_threading():
	q = Queue()
	threads = []
	data = [[1,2,3], [3,4,5], [4,4,4], [5,5,5]]
	results = []
	for i in range(4):
		t = threading.Thread(target=thread_job, args=(data[i],q))
		t.start()
		threads.append(t)
	for thread in threads:
		thread.join()
	for i in range(4):
		results.append(q.get())
	print(results)

if __name__ == '__main__':
	multi_threading()
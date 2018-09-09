# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-15 17:21:43
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-15 20:47:49

import time

def solve(nums, target, count, answer, f):
	if not nums or target <= 0 or count >= 6:
		if target == 0 and count == 6:
			output = [str(i) for i in answer]
			f.write("{},{},{},{},{},{}".format(output[0],output[1],output[2],output[3],output[4],output[5]))
			f.write('\n')
	else:
		solve(nums[1:], target, count, answer, f)
		answer.append(nums[0])
		solve(nums[1:], target-nums[0], count+1, answer, f)
		answer.pop()

if __name__ == '__main__':
	f = open('test_1.txt', 'w')
	start = time.time()

	nums = range(1, 37)
	target = 111
	answer = []

	solve(nums, target, 0, answer, f)

	print(time.time() - start)
	f.close()
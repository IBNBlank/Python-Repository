# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-25 14:30:19
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-25 14:31:36

with open("text.txt") as file:
	text_data = file.read()

with picamera.PiCamera() as camera
	camera.start_recording('video.h264')
	camera.wait_recording(120)
	camera.stop_recording()
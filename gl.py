# -*- coding: utf-8 -*-
from Queue import Queue
queue = Queue() #用于当作存放用户音频的队列，后面的处理线程从这个队列取数据

WAVPATH="/home/vincent/coding/python/piRobot/" #用于指定录音文件存放在什么地方

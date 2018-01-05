#!/usr/bin/python
#-*- coding: UTF-8 -*-

from math import sqrt
from sys import stdout

def judge_primNum(range_min,range_max):
	num=0
	flag=0

	for i in range(range_min,range_max):


		for j in range (2,int(sqrt(i)+1)):

			if i%j==0:
				flag=1
				break

		if flag==0:
			num+=1
			print('%4d' % i)

		flag=0

	print('%4d' % num)



judge_primNum(101,200)
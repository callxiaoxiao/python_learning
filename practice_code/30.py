#!/usr/bin/python
#-*- coding: UTF-8 -*-

a=int(input("input number:\n"))
x=str(a)
flag=True

for i in  range(int(len(x)/2)):
	print(int(len(x)/2),x[i],x[-i-1])
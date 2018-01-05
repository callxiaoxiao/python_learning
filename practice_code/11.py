#!/usr/bin/python
#-*- coding: UTF-8 -*-

def num():
	f1=1
	f2=1
	
	for i in range(1,22):
		print('%12ld  %12ld' % (f1,f2))
		f1=f1+f2
		f2=f1+f2
		#print('%12ld  %12ld' % (f1,f2))	

num()



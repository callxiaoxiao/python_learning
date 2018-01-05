#!/usr/bin/python
#-*- coding: UTF-8 -*-

for i in range (100,999):
	b=int(i/100)
	s=int(i/10 %10)
	g=int(i%10)
	#print('%d  %d  %d  %d' % (i,b,s,g))

	#print(i)
	#ret=b**3 + s**3 + g**3
	#print(ret)

	if i == (b**3 + s**3 + g**3):
		print(i)

    
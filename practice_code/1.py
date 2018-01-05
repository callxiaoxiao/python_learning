#!/usr/bin/python
#-*- coding: UTF-8 -*-

num=0;
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if (i!=j) and (j!=k) and (i!=k):
				result=i*100+j*10+k
				num=num+1

				print(result)

print(num)
			
		
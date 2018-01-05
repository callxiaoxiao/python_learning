#!/usr/bin/python
#-*- coding: UTF-8 -*-

score = int (input('input:\n'))

if score>=90:
	grade='A'
elif score >=60:
	grade='B'
else:
	grade='C'

print('%d belog to %s' %(score,grade))
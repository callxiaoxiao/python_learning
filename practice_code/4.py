#!/usr/bin/python
#-*- coding: UTF-8 -*-

year = int(input("year:"))
month = int(input("month:"))
day = int(input("day:"))
days = 0

months = (0,31,59,90,120,151,181,212,243,373,304,334)

if 0 < month <= 12:
	days = months[month-1]
else:
	print('data error')

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
	if month > 2:
		days=days+1

days+=day

print ("it is the %dth day." % days)

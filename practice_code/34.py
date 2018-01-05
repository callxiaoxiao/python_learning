#! /usr/bin/python
# coding：UTF-8

def hello_word():
	print('hello word')

def three_hellos():
	for i in range(3):
		hello_word()

if __name__ == '__main__':
	three_hellos()
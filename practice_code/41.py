#coding:UTF-8

def varfunv():
	var =0
	print ('var=%d'%var)
	var +=1

if __name__ == '__main__':
	for i in range(3):
		varfunv()


class Static:
	StaticVar=5

	def varfunc(self):
		self.StaticVar+=1
		print(self.StaticVar)


print (Static.StaticVar)

a=Static()

for i in range(3):
	a.varfunc()
		
#coding； UTF-8

if __name__ == '__main__':
	a=[1,2,3,4,5,6,7,8,9,0]

	for i in range(len(a)):
		print(a[i])

	number = int(input("input a number:\n"))
	end =a[8]
	if number > end:
		a[9]=number

	else:
		for i in range(len(a)-2):
			if number>=a[i] and number<a[i+1]:
				print()
				print('----',i+1)
				print()
				print(len(a))
				print()
				for x in range(len(a)-1,i+1,-1):
					print('----',x)
					print()
					a[x]=a[x-1]

				a[i+1]=number
				break

	for i in range(len(a)):
		print(a[i])


					



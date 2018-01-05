#coding； UTF-8

if __name__ == '__main__':
	a=[]
	sum=0

	for i in range(3):
		a.append([])

		for k in range(3):
			a[i].append(float(input('input number:\n')))

	for i in range(3):
		sum+=a[i][i]
	print(sum)
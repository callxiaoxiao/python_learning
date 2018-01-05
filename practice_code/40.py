#coding:UTF-8

if __name__ == '__main__':
	a=[1,2,3,4,5]
	N=len(a)-1

	for i in range(0,int(len(a)/2)):
		print(i)

		a[i],a[N-i]=a[N-i],a[i]

		print(a)

			
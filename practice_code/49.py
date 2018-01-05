
MAXMUM=lambda x,y:(x>y)*x+(x<y)*y
MINMUM=lambda x,y:(x>y)*y+(x<y)*x

if __name__ == '__main__':
	a=10
	b=20
	print(MAXMUM(a,b))
	print(MINMUM(a,b))


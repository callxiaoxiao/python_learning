
TRUE=1
FALSE=0

def SQ(x):
	return x*x
again=1
while again:
	num=int (input('number:\n'))

	if(SQ(num))>=50:
		again=TRUE
	else:
		again=FALSE
#constantpi.py - deitel python ch3 exercies 3.14
term = int(input('Enter term number: '))

pi = 0
x = 1

	
while(x <= term):
	print (x, end='\n')
	pi += 4*(1/x - 1/(x+2))
	x += 4
	print (pi, end='\n')

n = int(input(print('Enter term number: ')))

pi = 0
for n in range(1,n):
	pi = pi + 4*(1/n - 1/(n+2))
print (pi)

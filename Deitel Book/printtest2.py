#print testing - deitel python ch3 exercises 3.7

print('number','\t','square',' cube')

numbers = [0, 1, 2, 3, 4, 5]

for i in numbers:
	print(f'{i:>6}{i**2:>9}{i**3:>6}')

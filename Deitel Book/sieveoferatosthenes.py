#sieveoferatosthenes.py - deitel python ch5 exercies  5.8
import math

list = []
for i in range(1000):
	list.append(True)

for index in range(2,len(list)):
    if(index > int(math.sqrt(len(list)))):
        break
    else:
        if(list[index]):
            for j in range((index**2), len(list), index):
                    list[j] = False
        else:
            continue

for i in range(2, len(list)):
    if(list[i]):
    	print(f'{i:>3}')

#seperating numbers - deitel python ch2 exercises 2.11

number = int(input('Please enter a five-digit number: '))

print(number//10000,'\t',(number%10000)//1000,'\t',((number%10000)%1000)//100,'\t',(((number%10000)%1000)%100)//10,'\t',((((number%10000)%1000)%100)%10))

#cardshufflinganddealing.py deitel ch 5 ex 5.24
import random

face = ('Ace','Deuce','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
suit = ('Hearts','Diamonds','Clubs','Spades')
deck = []

for i in range(len(suit)):
    for j in range(len(face)):
        deck.append((face[j],suit[i]))

random.shuffle(deck)

i=0
while (i <= len(deck)):
    #print(i)
    print(f'{deck[i][0]} of {deck[i][1]:<10} {deck[i+1][0]} of {deck[i+1][1]:<10} {deck[i+2][0]} of {deck[i+2][1]:<10} {deck[i+3][0]} of {deck[i+3][1]}')
    i += 4
    if (i >= len(deck)):
        break


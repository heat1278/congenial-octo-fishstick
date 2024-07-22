#Creating a coin toss generator.

'''import random
coin = random.choice(["heads", "tails"])
print(coin)
'''

#Using the randint function to get a random number.
'''import random
number = random.randint (1,50)
print(number)
'''

#using the randint and loop function to keep generating random numbers until a specific number is generated.
'''import random

def generate_numbers():
    while True:
        number = random.randint(1, 100)
        print(f"Generated number: {number}")
        if number == 8:
            print("Number 8 has been generated. Stopping the loop.")
            break

generate_numbers()
'''

#Shuffling a set of cards in a list.
import random
cards = ["Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
for card in cards:
  print(card)
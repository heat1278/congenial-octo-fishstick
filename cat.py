#Example of using loops using while statments counting up.

'''i = 0
while i < 5:
  print("Meow")
  i += 1'''

#Example of using loops using for statments counting down.

'''i = 5
for i in range(5, 0, -1):
  print("Meow")'''

#Example of using a for loop to print out a list of numbers.
'''for i in [0, 1, 2, 3, 4]:
  print("Meow")'''

#Better code below as it is a simpler code for counting up from using Range.  _ allows you to use a variable that can/is to be ignored.
'''for _ in range(98):
  print("Meow")'''

#Example is using print multiplier
'''print ("Meow \n" * 3, end="")'''

#Example of using true loops intentionally.
'''while True:
  n = int(input("What's n? "))
  if n > 0:
    break

for _ in range(n):
  print("Meow")
'''

#Defining a new fuction called meow to log an input(number) and output out the number in meows.
def main():
  number = get_number()
  meow(number)

def get_number():
  while True:
    n = int(input("What's n? "))
    if n > 0:
      return n


def meow(n):
  for _ in range(n):
    print("Meow")

main()

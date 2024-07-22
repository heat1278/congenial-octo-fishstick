#Creating ways to protect code from errors (such as using a string when an interger is reqired.) by using try and except commands.

'''x = int(input("What's x? "))
print(f"X is {x}")'''

#The code below works, but would be cleaner using try, except, and an else command in case it fails.
'''try:
  x = int(input("What is x? "))
  print(f"X is {x}.")
except ValueError:
  print("Your input must be an interger")
'''

#Here is what may be best using the try, except, and else commands.
'''try:
  x = int(input("What is x? "))
except ValueError:
  print("X is not an interger")
else:
  print(f"X is {x}")'''

#Above code does not allow decimels such as 5.1.  Need to find a means to allow this.

#Using a loop to circle back to an input if the user does not enter a number.
'''while True:
  try:
    x = int(input("What is x? "))
  except ValueError:
    print("X is not an interger")
  else:
    break

print(f"X is {x}")'''

#using a define function to create a loop that will allow the user to enter a number.
def main():
  x = get_int()
  print(f"X is {x}")

def get_int():
  while True:
    try:
      x = int(input("What is x? "))
    except ValueError:
      print("X is not an interger")
    else:
      break
  return x

main()
'''Learning some code that saves/loads files to have persistent information.

names = []

for _ in range(3):
  name = input("What's your name? ")
  names.append(name)

for name in (sorted)names:
    print(f"Hello, {name}")

#Using the open function to create and allow a file to be writable.

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()

  #The above will log a name, but only a single input that is constantly overwritten because making files.txt writable ("w") essentially starts it over.  Instead, switch from w for write, to a for append.  After doing this, there's a new problem.  It's all one wall of text (each name written together rather than a line break on each.)

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

#This worked, but the file.close command is somewhat redundant when considering we can use the with command to close the file automatically.

name = input("What's your name? ")

with open("names.txt", "a") as file:
  file.write(f"{name}\n")

with open("names.txt", "r") as file:
  lines = file.readlines()

for line in lines:
  print ("Hello, ", line)

#This worked, but added an extra line break for some reason.  To fix this, we can use the strip command to remove the extra line break.

with open("names.txt", "r") as file:
  for line in file:
    print("Hello, ", line.strip())

#This worked, but doesn't let you sort the list that's been created.  So we'll have to start over in some sense.'''

name = []

with open("names.txt") as file:
  for line in file:
    name.append(line.strip())

for name in sorted(name):
  print(f"Hello, {name}.")
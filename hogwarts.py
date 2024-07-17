#Printing a list using  a for loop.
'''students = ("Ron", "Harry", "Hermione")

for student in students:
  print(student)
'''

#Using len to convert a list into an number, then printing the list
'''students = ("Ron", "Harry", "Hermione")

for i in range(len(students)):
  print(i + 1, students[i])
'''

#using dict function to convert a list into a dictionary.
'''
students = {
  "Hermione": "Gryffindor",
  "Harry": "Gryffindor",
  "Ron": "Gryffindor",
  "Draco": "Slytherin",
}

for student in students:
  print(student, students[student], sep=" is in ")
'''

#Using a three catagory list to print out a list of students and their houses, and patronus.
students = [
  {"Name": "Hermione", "House": "Gryffindor", "Patronus": "Otter"},
  {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
  {"Name": "Ron", "House": "Gryffindor", "Patronus": "Jack Russel Terrier"},
  {"Name": "Draco", "House": "Slytherin", "Patronus": None}
]

for student in students:
  print(student["Name"], student ["House"], student["Patronus"], sep=", ")

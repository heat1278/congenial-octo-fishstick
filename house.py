#Example of using match and case to tighten the list from if/elif/else statements.
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
  print ("Gryffindor")
    case "Draco":
  print ("Slytherin")
    case _:
  print ("Who?")
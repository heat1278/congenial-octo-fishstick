#Learning command line arguments using sys.argv.  Using except to ensure the parameter is filled with the users name.
'''import sys

try:
  print("Hello, my name is", sys.argv[1])
except IndexError:
  print("List your name when executing the code")
'''

#Tightening the code by using past education points with if, elif and else
'''import sys
if len(sys.argv) < 2:
  print ("Too few arguments")
elif len(sys.argv) > 2:
  print ("Too many arguments")
else:
  print("Hello, my name is", sys.argv[1])
'''

#Using sys.exit to prevent errors and cleaning up code to make it easier to read.
'''import sys
if len(sys.argv) < 2:
  sys.exit ("Too few arguments")
elif len(sys.argv) > 2:
  sys.exit ("Too many arguments")

print("Hello, my name is", sys.argv[1])
'''

#Using for function to use multiple names to print out multiple statements with the slice function.

import sys

if len(sys.argv) < 2:
  sys.exit ("Too few arguments")

#Remember that the first argument (0) is always the name of the script.  So start on argument 1 and to forward from there.
for arg in sys.argv[1:]:
  print("Hello, my name is", arg)
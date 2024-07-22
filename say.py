import sys

from sayings import hello

if len(sys.argv) == 2:
  hello(sys.argv[1])

'''The above will pull the entire main function from sayings.py and run it.  We can omit that by having the scripting below in the original sayings.py code.

if __name__ == "__main__":
  main()'''
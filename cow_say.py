import sys
import subprocess

#Function to install cowsay if not already installed
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import cowsay
except ImportError:
    install("cowsay")
    import cowsay

# Check if an argument is provided
if len(sys.argv) > 1:
    cowsay.trex("Hello, " + sys.argv[1])
else:
    print("Usage: python script_name.py [name]")
    print("Please provide a name as an argument.")
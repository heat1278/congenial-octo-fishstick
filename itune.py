#Api understanding.  Using requests package to pull web requests. 

import json
import sys
import subprocess

#Function to install requests if not already installed
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import requests
except ImportError:
    install("requests")
    import requests

if len(sys.argv) > 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])


'''print(json.dumps(response.json(), indent=2))'''
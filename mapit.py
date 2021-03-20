#! python3
"""mapit.py: lunches a map in the browser 
using the command line or the clipboard"""

import webbrowser 
import sys
import pyperclip
if len(sys.argv) > 1:
	#get address from the command line:
	address = " ".join(sys.argv[1:])
else:
	#get address from the paperclip
	address = pyperclip.paste()

webbrowser.open("https://www.google.co.uk/maps/place/"+address)
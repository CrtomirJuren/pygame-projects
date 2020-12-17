import os
from os import path

HIGHSCORE_FILE = "highscore.txt"

folder = path.dirname(__file__) #get application folder path

filename = path.join(folder, HIGHSCORE_FILE)
print(filename)

#if file exists, read from it
if os.path.exists(filename):
	with open(filename, 'r') as f:
		try:
			print("file opened")
			highscore = int(f.read())
			print(highscore)
		except:
			print("file read error")
# if file doesnt exists, create newread from it
else:
	with open(filename, 'w') as f:
		try:
			f.write("0")
		except:
			pass

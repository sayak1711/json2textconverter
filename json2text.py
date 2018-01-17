import json
import os
import codecs
from os import listdir
from os.path import isfile, join

def jsontotext(mypath):
	text_file = open("output_file.txt", "a", encoding="utf-8")
	filenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	for idx, val in enumerate(filenames):
		abs_path = os.path.abspath(mypath) + '/' + filenames[idx]
		with codecs.open(abs_path, "r", encoding="utf-8", errors="ignore") as myfile:
			jsonData = json.load(myfile)
			content = jsonData['translatedData']
			text_file.write(content)

	text_file.close()

if __name__ == "__main__":
	mypath = '' 			#enter within the quotes the path where you have the JSON files stored
	jsontotext(mypath)
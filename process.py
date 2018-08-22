# -*- coding: utf-8 -*-

# process.py

import os
import re

def count(_word, name=False):
	path = r"C:\Users\Max\Documents\Python\Worm_Webscraping"
	files = os.listdir(path)
	textfiles = [i for i in files if i.endswith(".txt")]
	word = bytes(_word, encoding="utf-8")
	
	total = 0
	for i in textfiles:
		with open("{path}\\{file}".format(path=path, file=i), "rb") as file:
			for line in file.readlines():
				words = line.split()
				total += words.count(word)
				if name:
					total += words.count(word + b"'s")
	return total


x = count("Taylor", name=False)
print(x)

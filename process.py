# -*- coding: utf-8 -*-

# process.py

import os
import re

def count_list(it, word):
	m = lambda a: re.match(word + r"\W*", a)
	l = tuple(filter(m, it))
	return len(l)

def count(word):
	path = os.path.dirname(os.path.abspath(__file__))
	files = os.listdir(path)
	textfiles = [i for i in files if i.endswith(".txt")]

	total = 0
	locations = []
	for i in textfiles:
		with open(os.path.join(path, i), "rb") as file:
			for linenumber, line in enumerate(file.readlines()):
				if linenumber > 0:
					textline = line.decode("utf-8")
					words = textline.split()
					c = count_list(words, word)
					if c:
						locations.append((i, linenumber))
						total += c

	return total


x = count("Amelia")
print(x)

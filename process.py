# -*- coding: utf-8 -*-

# process.py

import os
import re

def count_list(it, word):
	m = lambda a: re.match(a, (word + r"\W".encode("utf-8")))
	l = tuple(filter(m, it))
	return len(l)

def count(_word):
	path = os.path.dirname(os.path.abspath(__file__))
	files = os.listdir(path)
	textfiles = [i for i in files if i.endswith(".txt")]
	word = bytes(_word, encoding="utf-8")

	total = 0
	for i in textfiles:
		with open(os.path.join(path, i), "rb") as file:
			for line in file.readlines():
				words = line.split()
				total += count_list(words, word)

	return total


x = count("Taylor")
print(x)

import os
import re

inp = open("mbox-short.txt")
stringline = []

for line in inp:
	line = line.rstrip()
	newline = re.findall('^X-DSPAM-Confidence:\s([0-9.]*)' , line)
	if len(newline) != 0:
		stringline.append(float(newline[0]))
print('Number of Value:' , len(stringline))
print('Maximum:' , max(stringline))
print('Minimum:' , min(stringline))
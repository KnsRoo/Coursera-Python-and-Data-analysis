import numpy as np
import re
from scipy.spatial.distance import cosine


def notexists(words, word):
	ret = True
	for item in words:
		if item == word:
			ret = False
	return ret

def counts(words, word):
	count = 0
	i,j = 0,0
	for i in range(len(words)):
		for j in range(len(words[i])):
			if words[i][j] == word:
				count = count+1
	return count

def inputs(words, word):
	count = 0
	i,j = 0,0
	for i in range(len(words)):
		if words[i] == word:
			count = count+1
	return count



if __name__ == "__main__":
	f = open('sentences.txt', 'r')
	str1 = f.read()
	str1 = str1.lower()
	re.compile("[.!?\n]").split(str1)
	sentences = re.split("[.!?\n]", str1)
	for i in range(len(sentences)):
		while i < len(sentences):
			if sentences[i] == '':
				del sentences[i]
			else:
				i += 1
	a = []
	for item in sentences:
		words = re.split('[^a-z]', item)
		for i in range(len(words)):
			while i < len(words):
				if words[i] == '':
					del words[i]
				else:
					i += 1
		a.append(words)
	x = 0
	words2 = []
	d = {}
	sum = 0
	i,j= 0,0
	for i in range(len(a)):
		for j in range(len(a[i])):
			if notexists(words2, a[i][j]):
				d[a[i][j]] = 1
				words2.append(a[i][j])
				sum = sum+1
			else:
				c = counts(a, a[i][j])
				d[a[i][j]] = c
	M = np.zeros((22,254))
	for i in range(22):
		for j in range(254):
			M[i][j] = inputs(a[i], words2[j])
	result = []
	for i in range(22):
		result.append(cosine(M[0], M[i]))
	hlp = list(result)
	hlp.sort()
	answer = ''
	m1, m2 = hlp[1],hlp[2]
	for i in range(len(result)):
		if result[i] == m1 or result[i] == m2:
			answer = answer+str(i)+' '
	z = open('answer.txt', 'w')
	z.write(answer)
	z.close()
	f.close()

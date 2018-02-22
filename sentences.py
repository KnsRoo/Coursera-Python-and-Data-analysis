import numpy as np
import re
from scipy.spatial.distance import cosine

def notexists(words, word, ret = True):
	for item in words:
		if item == word:
			ret = False
	return ret

def inputs(words, word, count = 0):
	for i in range(len(words)):
		if words[i] == word:
			count = count+1
	return count

if __name__ == "__main__":

	a, words2, result, str1, answer = [], [], [], '', ''
	f,z = open('sentences.txt', 'r'), open('answer.txt', 'w')

	for line in f.readlines():
		str1 = str1+'\n'+line

	f.close()
	str1 = str1.lower(); sentences = re.split("[\n]", str1)

	for i in range(len(sentences)):
		while i < len(sentences):
			if sentences[i] == '':
				del sentences[i]
			else:
				i += 1

	for item in sentences:
		words = re.split('[^a-z]', item)
		for i in range(len(words)):
			while i < len(words):
				if words[i] == '':
					del words[i]
				else:
					i += 1
		a.append(words)

	for i in range(len(a)):
		for j in range(len(a[i])):
			if notexists(words2, a[i][j]):
				words2.append(a[i][j])

	p,q = len(a), len(words2)
	M = np.zeros((p,q))

	for i in range(p):
		for j in range(q):
			M[i][j] = inputs(a[i], words2[j])
	for i in range(p):
		result.append(cosine(M[0], M[i]))

	hlp = list(result); hlp.sort()
	m1, m2 = hlp[1],hlp[2]

	for i in range(len(result)):
		if result[i] == m1 or result[i] == m2:
			answer = answer+str(i)+' '

	z.write(answer)
	z.close()

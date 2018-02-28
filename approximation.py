import numpy as np
from scipy.linalg import solve
import math
import matplotlib.pyplot as plt

v1, v2, v3 = [], [], []

def f(x):
	return math.sin(x/5)*math.exp(x/10)+5*math.exp(-x/2)

def first(x1,x2):
	A = np.matrix([[1,x1],[1,x2]])
	print(A)
	n,m = f(x1), f(x2)
	B = np.array([n,m])
	global v1
	v1 = solve(A,B)
	print(v1)

def second(x1,x2,x3):
	A = np.matrix([[1,x1,x1**2],[1,x2,x2**2],[1,x3,x3**2]])
	print(A)
	n,m,p = f(x1), f(x2), f(x3)
	B = np.array([n,m,p])
	global v2
	v2 = solve(A,B)
	print(v2)

def third(x1,x2,x3,x4):
	A = np.matrix([[1,x1,x1**2,x1**3],[1,x2,x2**2,x2**3],[1,x3,x3**2,x3**3],[1,x4,x4**2,x4**3]])
	print(A)
	n,m,p,q = f(x1), f(x2), f(x3), f(x4)
	B = np.array([n,m,p,q])
	global v3
	v3 = solve(A,B)
	print(v3)

def drawplot():
	ax = np.arange(0,16,1)
	f2 = np.vectorize(f)
	plt.plot(ax, f2(ax))
	plt.plot(ax, v1[0]+v1[1]*ax)
	plt.plot(ax, v2[0]+v2[1]*ax+v2[2]*ax**2)
	plt.plot(ax, v3[0]+v3[1]*ax+v3[2]*ax**2+v3[3]*ax**3)
	plt.xlabel(r'$x$')
	plt.ylabel(r'$f(x)$')
	plt.grid(True)
	plt.show()

def write(x, ans = ''):
	for item in x:
		c = round(item,2); ans+=str(c)+' '

	f = open('answer2.txt', 'w')
	f.write(ans); f.close()

if __name__ == "__main__":
	first(1,15)
	second(1,8,15)
	third(1,4,8,15)
	drawplot()

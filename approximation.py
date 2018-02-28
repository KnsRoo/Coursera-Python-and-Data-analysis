import math, numpy as np, matplotlib.pyplot as plt
from scipy.linalg import solve

def f(x):
	return math.sin(x/5)*math.exp(x/10)+5*math.exp(-x/2)

def solve_sys(x1,x2,x3 = 'nil', x4 = 'nil', v = []):
	if x3 == 'nil':
		A = np.matrix([[1,x1],[1,x2]])
		n,m = f(x1), f(x2)
		B = np.array([n,m])
	elif x4 == 'nil':
		A = np.matrix([[1,x1,x1**2],[1,x2,x2**2],[1,x3,x3**2]])
		n,m,p = f(x1), f(x2), f(x3)
		B = np.array([n,m,p])
	else:
		A = np.matrix([[1,x1,x1**2,x1**3],[1,x2,x2**2,x2**3],[1,x3,x3**2,x3**3],[1,x4,x4**2,x4**3]])
		n,m,p,q = f(x1), f(x2), f(x3), f(x4)
		B = np.array([n,m,p,q])
	print(A)
	return solve(A,B)

def drawplot(v1,v2,v3, ax = np.arange(0,16,0.01), f2 = np.vectorize(f)):
	plt.plot(ax, f2(ax), ax, v1[0]+v1[1]*ax, ax, v2[0]+v2[1]*ax+v2[2]*ax**2, ax, v3[0]+v3[1]*ax+v3[2]*ax**2+v3[3]*ax**3)
	plt.xlabel(r'$x$'); plt.ylabel(r'$f(x)$')
	plt.grid(True)
	plt.show()

def write(x, ans = ''):
	for item in x:
		c = round(item,2); ans+=str(c)+' '
	f = open('answer2.txt', 'w')
	f.write(ans); f.close()

if __name__ == "__main__":
	v1, v2, v3 = solve_sys(1,15), solve_sys(1,8,15), solve_sys(1,4,8,15)
	print(v1); print(v2); print(v3);
	drawplot(v1,v2,v3)

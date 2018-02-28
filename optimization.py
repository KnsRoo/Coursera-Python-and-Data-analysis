import math, numpy as np, matplotlib.pyplot as plt
from scipy.optimize import minimize, differential_evolution as dE

def f(x):
	return math.sin(x/5)*math.exp(x/10)+5*math.exp(-x/2)
def g(x):
	return int(math.sin(x/5)*math.exp(x/10)+5*math.exp(-x/2))

def writefile(iter, ans):
	name = 'answer'+str(iter)+'.txt'
	f = open(name, 'w'); f.write(ans); f.close()
    
def drawplots(x1,x2, x = np.arange(1,30,0.01), f = np.vectorize(f), g = np.vectorize(g)):
	plt.plot(x, f(x), x, g(x))
	plt.xlabel(r'$x$'); plt.ylabel(r'$f(x)$')
	plt.grid(True)
	plt.show()

if __name__ == "__main__":
	x1,x2 = 2, 30
	a,b = minimize(f, x1, method = 'BFGS'), minimize(f, x2, method = 'BFGS') 
	a,b = round(a.fun,2), round(b.fun,2)
	writefile(3, str(a)+' '+str(b))
	a = dE(f,[(x1,x2)]); a = round(a.fun,2)
	writefile(4, str(a))
	a,b = minimize(g, x2 ,method = 'BFGS'), dE(g,[(x1,x2)])
	writefile(5, str(int(a.fun))+' '+str(int(b.fun)))
	drawplots(1,30)

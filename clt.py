import numpy as np
import scipy.stats as sts
import pandas as pd
import matplotlib.pyplot as plt
import math

def drawplot(x, mas, dis):
	df = pd.DataFrame(mas, columns=['Плотность'])
	ax = df.plot(kind='density')
	plt.hist(mas, normed=True, label='Выборка')
	plt.plot(x, dis.pdf(x),label='Теоретическая плотность')
	plt.legend()
	plt.ylabel('$f(x)$')
	plt.xlabel('$x$')

def generate(x, Mx, Sg, dist, dist_size, counts = 1000):
	a = []
	for i in range(counts):
		new_dist = dist[np.random.randint(0,len(dist),dist_size)]
		a.append(np.mean(new_dist))
    
	mu = np.mean(a)
	sigma = np.std(a,ddof=1)
	SE = Sg/math.sqrt(dist_size) # стандартная ошибка среднего
	normal_dist = sts.norm(Mx,SE)
    
	SE = round(SE,2); sigma = round(sigma,2); mu = round(mu,2)
    
	print("Теоретическое среднее "+str(Mx)+"\nПриближенное среднее "+str(mu))
	print("Теоретическое ст. отклонение "+str(SE)+"\nПриближенное стандартное отклонение "+str(sigma))
	print("Доверительный интервал "+str(mu)+" \033[4m+\033[0m "+str(2*SE))

	drawplot(x, a, normal_dist)


if __name__ == "__main__":
	k = 3
	distrib = sts.chi2(k)
	dist = distrib.rvs(1000)
	x = np.linspace(0,20,100)
	Mx, Dx= k, 2*k
	Sg = math.sqrt(Dx)

	drawplot(x, dist, distrib)

	lst = [5, 10, 50]
	for item in lst:
		generate(x, Mx, Sg, dist, item)

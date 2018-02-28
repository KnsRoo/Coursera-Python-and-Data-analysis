import math, numpy as np, scipy.stats as sts, pandas as pd, matplotlib.pyplot as plt

def drawplot(x, mas, dis):
	df = pd.DataFrame(mas, columns=['Плотность'])
	ax = df.plot(kind='density')
	plt.hist(mas, normed=True, label='Выборка')
	plt.plot(x, dis.pdf(x),label='Теоретическая плотность')
	plt.legend(); plt.ylabel('$f(x)$'); plt.xlabel('$x$')

def generate(x, Mx, Sg, dist, dist_size, out, counts = 1000, a = []):
	for i in range(counts):
		new_dist = dist[np.random.randint(0,len(dist),dist_size)]
		a.append(np.mean(new_dist))
    
	mu, sigma, SE = np.mean(a), np.std(a,ddof=1), Sg/math.sqrt(dist_size)
	normal_dist = sts.norm(Mx,SE)
    
	SE = round(SE,2); sigma = round(sigma,2); mu = round(mu,2)

	drawplot(x, a, normal_dist)
    
	print(str(out)+" график:")
	print("Теоретическое среднее vs Приближенное среднее: "+str(Mx)+" vs "+str(mu))
	print("Теоретическое ст. отклонение vs Приближенное ст. отклонение: "+str(SE)+" vs "+str(sigma))
	print("Доверительный интервал: "+str(Mx)+" \033[4m+\033[0m "+str(2*SE)); print('-'*30)   


if __name__ == "__main__":
	k, i, lst = 3, 2, [5, 10, 50]
	distrib = sts.chi2(k)
	dist = distrib.rvs(1000)
	x = np.linspace(0,20,100)
	Mx, Dx= k, 2*k
	Sg = math.sqrt(Dx)

	drawplot(x, dist, distrib)

	for item in lst:
		generate(x, Mx, Sg, dist, item, i); i+=1;

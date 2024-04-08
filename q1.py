from numpy.random import multivariate_normal 

def gen_normal_2d(mean1=5,mean2=30,var1=1,var2=20,covariance=-1,size=1000):
	mean = [mean1, mean2]
	covar = [[var1,covariance],[covariance,var2]]
	return multivariate_normal(mean,covar,size)

if __name__=='__main__' :
	#################
	from collections import Counter

	mean1 = float(input("Enter the Mean of DIM1, μ1 : "))
	var1 = float(input("Enter the Standard Deviation of DIM1, σ2 : "))
	mean2 = float(input("Enter the Mean of DIM2, μ2 : "))
	var2 = float(input("Enter the Standard Deviation of DIM2, σ1 : "))
	size = int(input("Enter the number of points to be generated : "))

	#mean1 = 30
	#var1 = 15
	#mean2 = 5
	#var2 = 2
	#size = 800

	df = gen_normal_2d(mean1,mean2,var1,var2,size=size)
	x = [int(item[0]) for item in df]
	y = [int(item[1]) for item in df]
	x = Counter(x)
	y = Counter(y)

	x = [[value,x[value]] for value in x]
	y = [[value,y[value]] for value in y]

	# plotting data 
	from matplotlib import pyplot as plt

	fig = plt.figure(figsize=(12,8))
	ax = fig.add_gridspec(2,2)

	subplot_0_01 = fig.add_subplot(ax[0,:])
	subplot_0_01.scatter([item[0] for item in df],[item[1] for item in df],color='maroon')
	subplot_0_01.set_xlabel("DIM1 : (μ=%d,σ=%d)"%(mean1,var1))
	subplot_0_01.set_ylabel("DIM2 : (μ=%d,σ=%d)"%(mean2,var2))


	subplot_1_0 = fig.add_subplot(ax[1,0])
	subplot_1_0.bar([item[0] for item in x],[item[1] for item in x],color='grey')
	subplot_1_0.set_xlabel("Distribution of DIM1 (μ=%d,σ=%d)"%(mean1,var1))
	subplot_1_0.set_ylabel("Frequency"	)

	subplot_1_1 = fig.add_subplot(ax[1,1])
	subplot_1_1.bar([item[0] for item in y],[item[1] for item in y],color='grey')
	subplot_1_1.set_xlabel("Distribution of DIM2 (μ=%d,σ=%d)"%(mean2,var2))

	plt.show()
	##################
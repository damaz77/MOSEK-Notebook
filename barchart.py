import numpy as np
import matplotlib.pyplot as plt

def plot_bar(xx, c, title, xlabel, ylabel):
	n = len(xx)
	ind = np.arange(n)
	width = 1
	fig, ax = plt.subplots()
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	ax.set_xticks(ind + 0.5)
	ax.set_xticklabels(ind)
	rects1 = ax.bar(ind, xx, width, color=c)
	if np.abs(np.min(xx))> np.abs(np.max(xx)):
		bound = np.abs(np.min(xx))
	else:
		bound = np.abs(np.max(xx))
	if(np.min(xx)<0):
		plt.axis([0, n, -1.1*bound, 1.1*bound])
	else:
		plt.axis([0, n, 0, 1.1*bound])
	plt.show()
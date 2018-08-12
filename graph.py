# importing the required module
import matplotlib.pyplot as plt
from identifier import know_index

def graph(this): 
	path = 'data/'+know_index(this)+'.txt'
	with open(path) as f:
		content = f.readlines()
	
	y = [float(x.strip()) for x in content]
		
	# x axis values
	x = []
	for i in range(len(y)):
		x.append(i+1)
 
	# plotting the points 
	plt.plot(x, y)
 
	# naming the x axis
	plt.xlabel('data-index')
	# naming the y axis
	plt.ylabel('max-trade-price')
 
	# giving a title to my graph
	plt.title(know_index(this))
 
	# function to show the plot
	plt.show() 	

graph("NLIC")

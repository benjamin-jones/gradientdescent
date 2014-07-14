#!/usr/bin/python
import sys
import csv
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
class Point:
	def __init__(self,x,y):
		self.x = float(x)
		self.y = float(y)
	def getX(self):
		return self.x
	def getY(self):
		return self.y



def computeTotalError(m,b,points):
	totalError = 0
	for point in points:
		totalError += (point.getY() - (m*point.getX() + b))**2
	return totalError / float(len(points))


def main():
	raw_points = []

	with open('points.csv') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			raw_points.append(row)
	points = []
	for x,y in zip(raw_points[0], raw_points[1]):
		points.append(Point(x,y))
	
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	M = np.arange(-5,5,0.5)
	B = np.arange(-5,5,0.5)
	M,B = np.meshgrid(M,B)
	Z = np.zeros( (1,len(M)))
	Z = computeTotalError(M,B,points)
	surf = ax.plot_surface(M,B,Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)

	plt.show()
		

if __name__=="__main__":
	main()

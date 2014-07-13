#!/usr/bin/python
import csv
import math
import random

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

def stepGradient(b_current, m_current, points, learningRate):
	b_gradient = 0.0
	m_gradient = 0.0
	N = float(len(points))

	for point in points:
		b_gradient += -(2.0/N) * (point.getY() - ((m_current*point.getX()) + b_current))
		m_gradient += -(2.0/N) * point.getX() * (point.getY() - ((m_current*point.getX()) + b_current))

	
	new_b = b_current - (learningRate * b_gradient)
	new_m = m_current - (learningRate * m_gradient)

	return [new_b, new_m]


def computeDescent(points,params):
	m = params[0]
	b = params[1]

	b_current = random.randrange(-10,10)
	m_current = random.randrange(-10,10)
	learningRate = 0.005

	iterations = 0

	while abs(b_current - b) > 0.00001 and abs(m_current - m) > 0.00001:
		b_current, m_current = stepGradient(b_current, m_current, points, learningRate)
		print "Moving to (%f,%f)" % (m_current, b_current)
		iterations += 1
	return [b_current, m_current, iterations]
		


def main():
	try:
		raw_points = []
		points = []
		params = []
		with open('points.csv') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				raw_points.append(row)
		with open('answer.csv') as csvfile:
			reader = csv.reader(csvfile)
			for param in reader:
				params.append(float(param[0]))
		for x,y in zip(raw_points[0], raw_points[1]):
				points.append(Point(x,y))

		print computeDescent(points,params)
	except IOError:
		print "IOError with file"
		exit(-1)
	except KeyboardInterrupt:
		print "Exiting!"
		exit(0)
	except ValueError:
		print "Value Error!"
		exit(-1)
	except OverflowError:
		print "Overflow!"
		exit(-1)
	return	

if __name__=="__main__":
	main()
	exit(0)


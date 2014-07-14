#!/usr/bin/python
import csv
import math
import random
import threading

class Point:
	def __init__(self,x,y):
		self.x = float(x)
		self.y = float(y)
	def getX(self):
		return self.x
	def getY(self):
		return self.y

class walkThread(threading.Thread):
	def __init__(self, tid, name, points, params):
		threading.Thread.__init__(self)
		self.tid = tid
		self.name = name
		self.points = points
		self.params = params
		self.result = []
	def run(self):
		self.result = computeDescent(self.points,self.params)
	def getResult(self):
		return self.result
	def getName(self):
		return self.name

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

	while abs(b_current - b) > 0.00001 and abs(m_current - m) > 0.00001 and iterations < 5000:
		b_current, m_current = stepGradient(b_current, m_current, points, learningRate)
		iterations += 1
	return [m_current, b_current, iterations]
		


def main():
	try:
		raw_points = []
		points = []
		params = []
		threads = []
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

		for i in range(0,10):
			threads.append(walkThread(i, "Walker-"+str(i), points, params))
		
		print "Starting the walkers..."

		for thread in threads:
			thread.start()

		for thread in threads:
			thread.join()

		for thread in threads:
			print thread.getName() + " got ",
			print thread.getResult() 

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


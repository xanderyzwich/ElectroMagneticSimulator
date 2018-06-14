import numpy as num
import scipy as sci
import math as m

class Simulation():
	
	#int x, y , z	#size
	#int xoffset, yoffset, zoffset	#half size for axial reference
	#int[] xSet, ySet, zSet	#will construct the set of values for looping
	
	#the integer values will be handled as milimeters
	#the GUI handler will intake sizes in meters
	#the sizes given here are for the space and not the object
	def _init_(self, length, width, height):
		z = height	#z-size
		x = length	#x-size
		y = width	#y-size
		
		#the offset will be used to reference the axes of the space
		zoffset = z/2
		xoffset = x/2
		yoffset = y/2
		
		#this creates an empty space of given dimension
		#space has x, y, and z axes at offsets
		#the positions will be used as points not boxes
		#this convention will help represent cartesian coordinates
		self.space = zeros((x+1, y+1, z+1))
		
	#run simulation
	def simulate(self):
		raise NotImplementedError("You forgot to implement me!")
		#import image as a layer of the space
		#numpy must use .png
		#imports as float32 values from 0.0 to 1.0
		
		#extend  object along z-axis
		#using insert function
		
		#populate space with field values
		#using interrogateMagnitude function
	
		
	#insert a point charge into the space
	#will be used to create objects as well	
	def insert(self, inputX, inputY, inputZ, magnitude):
		self.space[inputX, inputY, inputZ] = magnitude
		
	#will find the vector representation of field at given point for unit charge	
	def interrogate(self, inputX, inputY, inputZ):
		xval=yval=zval=float()
		raise NotImplementedError("You forgot to implement me!")
		return (xval, yval, zval)
	
	#will find the magnitude of field on a given interrogation point	 
	def interrogateMagnitude(self, inputX, inputY, inputZ):
		a = interrogate(inputX, inputY, inputZ)
		#vectorLength^2 = X^2+Y^2+Z^2
		vectorLength=m.sqrt(a[0]**2+a[1]**2+a[2]**2)
		return vectorLength

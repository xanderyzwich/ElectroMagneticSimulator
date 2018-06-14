import numpy as num
import scipy as sci
import math as m
import tools

class Simulation:
	
	
	# epsilon=8.854e-12
	# int x, y , z	#size
	# int xoffset, yoffset, zoffset	#half size for axial reference
	# int[] xSet, ySet, zSet	#will construct the set of values for looping
	
	# the integer values will be handled as milimeters
	# the GUI handler will intake sizes in meters
	# the sizes given here are for the space and not the object
	def __init__(self, length, width, height, image, magnitude, infinite):
		
		
		# set sizes
		self.x = length	#x-size
		self.y = width	#y-size
		self.z = height	#z-size
		
		# set array sizes
		self.x1=length+1
		self.y1=width+1
		self.z1=height+1
		
		# the offset will be used to reference the axes of the space
		self.zoffset = (self.z/2)+1
		self.xoffset = (self.x/2)+1
		self.yoffset = (self.y/2)+1
		
		i=image
		mag=magnitude
		inf=infinite
		
		# this creates an empty space of given dimension
		# space has x, y, and z axes at offsets
		# the positions will be used as points not boxes
		# this convention will help represent cartesian coordinates
		self.space = num.zeros((self.x1, self.y1, self.z1))
		
#		self.simulate(image,magnitude,infinite)
		
		
		
	# run simulation
	# image is a string for the name of the black and white image
	# magnitude is the magnitude of the constant distribution
	def simulate(self, image, magnitude, infinite):
		# import image as a 2-Dimensional array
		# numpy must use .png
		# imports as float32 values from 255
		# then normalized to binary to scale to a linear magnitude
		# could be scaled using a loops for non-constant distributions
		layer = tools.read(image)
		layer = layer/255
		layer = layer*magnitude
		
		#extend  object along z-axis
		#using insert function
		self.extend(layer, infinite)
			
		
		#self.field()
	
	
	# this will be used to extend the layer along the z-axis
	# layer is the 2-Dimensional array
	# infinite will be a boolean 
	# infinite= true for infinite wire/cylinder/box
	def extend(self, layer, infinite):
		
		
		if (infinite):
			# a is loop control and b is stopping point
			a=0
			b=self.z1
		else:
			a=(elf.z/3)
			b=a*2
		while a<b:
			self.space[:,:,a]=layer
			a+=1
	
	#	Constant complexity
	#	
	#insert a point charge into the space
	#will be used to create objects as well	
	def insert(self, inputX, inputY, inputZ, magnitude):
		self.space[inputX, inputY, inputZ] = magnitude
	
	
	#	n^3 complex
	#	
	# will find the vector representation of field at given point for unit charge
	# if cartesian== true inputs for X,Y,Z are in standard cartesian coordinates
	# cartesian(0,0,0) == space(Xoffset,Yoffset,Zoffset)	
	def interrogate(self, cartX, cartY, cartZ):
		cartesian=0
		if (cartesian):
			X=cartX+self.xoffset
			Y=cartY+self.yoffset
			Z=cartY+self.zoffset
		else:
			X=cartX
			Y=cartY
			Z=cartZ
		v=tools.blank()
		k=tools.k()
		##	formula E=(Rvect)kq/(Rmag)^2
		##	triple nest loop to travel the space 
		i=0
		while i<self.x1:
			j=0
			while j<self.y1:
				k=0
				while k<self.z1:
					if self.space[i,j,k] != 0:
						Rad=tools.rad(i,j,k,X,Y,Z)
						Rmag=tools.magnitude(Rad)
						Runit=tools.unitrad(Rad)
						E=(Rvect*k*self.space(i,j,k))/(Rmag**2)
						v= v + E
		##	continue looping
					k+=1
						
				j+=1
			i+=1
		return v
	
	
	#will find the magnitude of field on a given interrogation point	 
	def interrogateMagnitude(self, inputX, inputY, inputZ):
		a = self.interrogate(inputX, inputY, inputZ)
		#vectorLength^2 = X^2+Y^2+Z^2
		vectorLength=m.sqrt(a[0]**2+a[1]**2+a[2]**2)
		return vectorLength
		
	#	n^6 complexity
	#	use not advisable
	#
	# this new function will create the field space and fill it with the magnitude
	# the field will conatin float values 
	# the field space is only rendered in places where the object isn't
	# the field space will have zero values everywhere the object is
	# this will allow for hard contrast 0-255 at the object's borders
	def field(self):
		fieldSpace=num.zeros((self.x,self.y,self.z))
		# loop through 3space and interrogateMagnitude at all points
		# for points outside the object
		i=0
		while i<self.x1:
			j=0
			while j<self.y1:
				k=0
				while k<self.z1:
					if self.space[i,j,k] != 0:
						fieldSpace[i,j,k]=self.interrogateMagnitude(i,j,k)
		##	continue looping
					k+=1
						
				j+=1
			i+=1
		return fieldSpace
	
	#	n^5 complexity
	#
	# this will render a central layer of the field space
	# use in order artificially render field space of infinite objects
	def fieldLayer(self):
		fieldLayer=num.zeros((self.x1,self.y1))
		i=0
		while i<self.x1:
			j=0
			while j<self.y1:
				if self.space[i,j,self.zoffset] != 0:
					fieldLayer[i,j]=self.interrogateMagnitude(i,j,self.zoffset)
					print j
		##	continue looping
				j+=1
			i+=1
		return fieldLayer

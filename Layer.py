import numpy as np
from scipy.misc import toimage

#	this creates a 2D layer to be used in the space class
class Layer:
	def __init__(self, size):
		self.s=size
		self.s1=size+1
		self.s2=(size/2)+1
		self.s4=size/4
		self.shape=np.array((self.s1,self.s1))
		self.space=np.zeros((self.s1,self.s1))
	
	def insert(self,x,y,value):
		self.space[x,y]=value
	
	def mirror8(self,x,y,value):
		## this considers 4 lines of symmetry
		## (x,y)&(y,x) mirrors across y=x
		## (x,y)&(x2,y) mirrors left to right
		## (x,y)&(x,y2) mirrors top to bottom
		## (x,y)&(x2,y2) mirrors across x+y=max
		if value==0:
			return
		x2=self.s-x
		y2=self.s-y
		self.space[x,y]=value
		self.space[y,x]=value
		self.space[x,y2]=value
		self.space[y2,x]=value
		self.space[x2,y]=value
		self.space[y,x2]=value
		self.space[x2,y2]=value
		self.space[y2,x2]=value

	def mirror4(self,x,y,value):
		if value==0:
			return
		# this just considers mirror in vertical and horizontal
		x2=self.s-x
		y2=self.s-y
		self.space[x,y]=value
		self.space[x,y2]=value
		self.space[x2,y]=value
		self.space[x2,y2]=value

	def mirror2(self,x,y,value):
		# mirrors only in x
		if value==0:
			return
		x2=self.s-x
		self.space[x,y]=value
		self.space[x2,y]=value
	
	def show(self):
		toimage(self.space).show()

	def getmax(self):
		maximum=0.0
		i=0
		while i<=self.s1:
			j=0
			while j<-self.s1:
				if self.space[i,j]>maximum:
					maximum=self.space[i,j]
				j+=1
			i+=1
		return maximum

	def getmin (self):
		minimum=0.0
		i=0
		while i<=self.s1:
			j=0
			while j<-self.s1:
				if self.space[i,j]<minimum:
					minimum=self.space[i,j]
				j+=1
			i+=1
		return minimum
		

import numpy as np

class Space:
	def __init__(self,layer,infinite):
		self.infinite=infinite
		self.layer=layer
		self.size=layer.shape[0]
		self.half=((self.size-1)/2)+1
		self.shape=np.array((self.size,self.size,self.size))
		self.matrix=np.zeros(self.shape)
		self.extend()
		
	def extend(self):
		## this has been phased out
		if self.infinite:
			i=0
			b=self.size
		else:
			i=(self.size-1)/3
			b=self.size-i
		while i<b:
			self.matrix[:,:,i]=self.layer.space
			
	def insert(self,x,y,z,value):
		self.matrix[x,y,z]=value
		
	def mirror(self,x,y,z, value):
		x2=self.size-x
		y2=self.size-y
		z2=self.size-z
		self.matrix[x,y,z]=value
		self.matrix[x,y,z2]=value
		self.matrix[x,y2,z]=value
		self.matrix[x,y2,z2]=value
		self.matrix[x2,y,z]=value
		self.matrix[x2,y,z2]=value
		self.matrix[x2,y2,z]=value
		self.matrix[x2,y2,z2]=value
		
		

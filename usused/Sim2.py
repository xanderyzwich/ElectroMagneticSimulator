import numpy as np
import tools
from Layer import *
import math


class Simulation:

	def __init__(self,infinite=1,image="wire",size=200,magnitude=1.6*(10**-19)):
		# image chooses the type of object that is being simulated
		# pictures is a boolean for rendering 3 views of the field
		self.s=size
		self.s1=size+1
		self.s2=size/2
		self.s3=math.floor(size/3)
		self.offset=(size/2)+1
		self.magnitude=magnitude  #this is voltage difference for plates
		self.infinite=infinite
		self.image=image
		self.layer = self.draw(image)
		self.top=Layer(self.s)
		self.front=Layer(self.s)
		self.side=Layer(self.s)
	
	def interrogate(self,x,y,z,bloat=0):
		x1=x+self.offset
		y1=y+self.offset
		v=tools.blank()		# this will collect the vector of the E-field 
		if self.inside(x,y,z):
			return tools.blank()
		elif self.image=="plates":
			a=self.s3
			b=self.s1-self.s3
			if a<=x<=b:
				return np.array(1,0,0)*(self.magnitude/(b-a))
		elif self.infinite:
			# use (lambda)/(2piE0R)
			c= self.magnitude/(2*tools.pi()*tools.E0())
			if x1<self.s3:
				r= math.sqrt((self.s3-x)**2+(self.s3-y)**2)
			else:
				r= (self.s3-y)
			v=tools.unitrad(np.array((x,y,0)))
			return v * float(c/r)
		elif bloat:
			if x<self.s3:
				delta=x1-y1
				side=self.s1-2*self.s3
				short=side-delta
				c=math.ceil(delta/2)
				delta2=math.floor(delta/2)
				A=side**2
				A1=short*short
				A2=delta*side+(.5*delta*delta)
				## position of cetroid in a trapazoid
				h=((side+(2*short))/(3*(short+side)))*delta
				cornerx=self.s3+h
				cornery=self.s1-cornerx
				y2=0.5*(self.s3+cornery)
				x2=0.5*(self.s1-self.s3+cornerx)
				c2x=round(0.5*(cornerx+x2))
				c2y=round(0.5*(cornery+y2))
				C1=self.offset+c
				v1=tools.field(C1,C1,0,x1,y1,z,(A1/A)*self.magnitude)
				v2=tools.field(c2x,c2y,0,x1,y1,z,(A2/A)*self.magnitude)
				return (v1+v2)

			if self.s3<=x1<=self.offset and y<=self.s3:
				delta=x1-self.s3
				g=2*x1-self.s3
				height=self.s1-(2*self.s3)
				A=height**2
				A1=(2*(x1-self.s3)*height)
				A2=A-A1
				i=x1
				j=self.offset
				k=0
				v1=tools.field(i,j,k,x1,y1,z,(A1/A)*self.magnitude)
				CentroidX2=round(.5*(g+self.s1-self.s3))
				v2=tools.field(CentroidX2,j,k,x1,y1,z,(A2/A)*self.magnitude)
				return (v1+v2)

	def draw(self,image):
		layer=Layer(self.s1)
		self.count=0
		self.square=0
		if image=="wire":
			layer.insert(self.offset,self.offset,self.magnitude)
		
		elif image=="box":
			# draws hollow square with side= size/3
			# linear n/6
			self.square=1
			x=(self.s3)
			while x<=self.offset:
				layer.mirror8(x,self.s3,self.magnitude)
				self.count+=8
				x+=1
		
		elif image=="block":
			# draws solid block 
			# draws smaller box just inside last box
			# repeats until fully shaded
			# linear (1/72)(x^2+x)
			self.square=1	
			x=(self.s/3)
			while x<=self.offset:
				y=x
				while y<=self.offset:
					layer.mirror8(x,y,self.magnitude)
					self.count+=8
					y+=1
				x+=1
		
		elif image=="tube":
			# draws a circle with radius r about point a
			# linear n/12 runtime
			x=float(self.s3)
			a=float(self.offset)
			r=a-x
			while x<=a:
				g=(x-a)**2
				y=round(a+math.sqrt(r**2-g))
				layer.mirror8(x,y,self.magnitude)
				layer.mirror8(x,y-1,self.magnitude)
				self.count+=16
				x+=1
		
		elif image=="rod":
			# draws a solid cylinder
			## runs at (pi*n^2)/72
			x=float(self.s3)
			a=float(self.offset)
			r=a-x
			while x<=a:
				g=(x-a)**2
				y=round(a-math.sqrt(r**2-g))
				layer.mirror8(x,y,self.magnitude)
				self.count+=8
				while y<=a:
					layer.mirror8(x,y,self.magnitude)
					self.count+=8
					y+=1
				x+=1
	
		elif image=="plates":
			x=self.s3
			y=0
			while y<self.offset:
				layer.mirror4(x,y,self.magnitude)
				y+=1
		
		#layer.show()
		self.count-=7
		return layer

	def render(self):
		i=-self.offset
		k=i+self.s3
		while i<=0:
			x=i+self.offset
			j=-self.offset
			while j<=i:
				y=j+self.offset
				temp=self.interrogate(i,j,0,self.square)
				temp=tools.magnitude(temp)
				self.top.mirror8(x,y,temp)
				if self.infinite==0:	
					temp=self.interrogate(0,i,j,1)
					temp=tools.magnitude(temp)
					self.side.mirror8(x,y,temp)
					# temp=self.interrogate(i,0,j,1)
					# temp=tools.magnitude(temp)
					# self.front.mirror4(x,y,temp)
				j+=1
			i+=1
		self.side.show()
		v1=self.top.space[self.offset,:]
		v2=self.top.space[:,self.offset]
		if self.infinite:
			i=0
			while i<self.s1:
				self.side.space[:,i]=v1
				self.front.space[i,:]=v2
				i+=1
		
		self.top.show()
		self.side.show()
		if self.infinite:
			self.front.show()
	
	def inside(self,x,y,z):
		x1=x+self.offset
		y1=y+self.offset
		true=1
		false=0
		a=self.offset-self.s3
		if self.infinite==0:
			if abs(z)>a:
				return false
		if self.image=="tube":
			r=float(self.offset)-float(self.s3)
			if math.sqrt(x**2+y**2)<=r:
				return true
		elif self.image=="box":
			if x1>=self.s3:
				if y1>=self.s3:
					return true
		elif self.image=="plates":
			if x1>=self.s3:
				temp=self.s1-self.s3
				if x1<=temp:
					return true
		elif self.layer.space[x1,y1]:
			return true
		else:
			return false

from layers import *
from layer import *
from numpy import array,zeros
import tools

class Simulation:
	def __init__(self,image,charge=0,infinite=0,size=0.2):
		self.infinite=infinite
		self.image=image.lower()
		self.realSize=size
		self.size=size*1e3
		self.transition=self.realSize*10
		self.charge=charge
		self.thing=None
		
		
		## create the charged object in 2D
		if image=='wire':
			self.thing=Wire(self.size)
		elif image=='box':
			self.thing=Box(self.size)
		elif image=='block':
			self.thing=Block(self.size)
		elif image=='tube':
			self.thing=Tube(self.size)
		elif image=='rod':
			self.thing=Rod(self.size)
		elif image=='plates':
			self.thing=Plates(self.size)
		else:
			self.thing=Block(self.size)

		# apply the proper charge to the object
		if self.charge==0:
			electron=1.6021765e-19
			charge=size*self.thing.count*electron
		if not self.infinite:
			self.thing.scale(self.charge)
		else:
			# for infinite "wire" the linear charge distribution
			# will be coulombs per meter
			# 1000 layers per meter
			self.thing.scale(self.charge*1e-3)
		#self.start()

	def start (self):
		# this method finds the magnitude of the field
		# on the positive x side of the object
		# this will later be used to cheat other calculations
		# the cheats are based on known equipotential lines around the object
		# and how to draw them
		self.E1=0.0
		temp=0.0
		i=self.thing.small
		p1=(self.thing.small,0,0)
		while i<self.thing.size:
			print i
			j=self.thing.small
			while j<0:
				k=self.thing.small
				while k<=0:
					p2= (self.thing.small+i,j,k)
					radius=tools.radv(p2,p1)
					x=tools.unitrad(radius)
					mag=tools.field(self.thing.image[i,j],tools.magnitude(radius))
					self.E1+=4*mag*x[0]
					k+=1
				j+=1
			i+=1

	def draw(self):
		g=50	# pixels per meter
		end=tools.fieldr(self.charge,0.1*self.E1)*g
		l=(2*end)
		self.top=layer(l)
		self.side=layer(l)
		h=0.1
		while h<1:
			r=tools.fieldr(self.charge,h*self.E1)*g
			print "At ",r," meters away E=",h*self.E1
			x=floor(sqrt(0.5*(r**2)))
			while x>=self.top.s2:
				if r<self.transition:
					sidey=tools.gety(x,r,self.top.s2-(self.realSize/2))
					if self.thing.square and x<self.top.s2+(self.realSize/2):
						topy=self.top.s2-(self.realSize/2)-r
					else:
						topy=sidey
				else:
					sidey=tools.gety(x,r,self.top.s2)
					topy=sidey
				self.top.mirror8(x,topy,h*self.E1)
				self.side.mirror8(x,sidey,h*self.E1)
				x-=1
			h+=0.1
		if self.infinite:
			q=self.top.space[:,self.top.s2]
			i=0
			while i<self.side.s1:
				self.side.space[:,i]=q
				i+=1
		

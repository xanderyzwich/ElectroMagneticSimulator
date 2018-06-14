def start (self):
		# this method finds the magnitude of the field
		# on the positive x side of the object
		# this will later be used to cheat other calculations
		# the cheats are based on known equipotential lines around the object
		# and how to draw them
		self.E1=0.0
		temp=0.0
		i=self.thing.small+1
		p1=(self.thing.small,0,0)
		j=self.thing.small
		while j<0:
			k=self.thing.small
			while k<=0:
				p2= (self.thing.small+i,j,k)
				radius=tools.radv(p2,p1)
				x=tools.unitrad(radius)
				mag=tools.field(self.thing.get(i,j),tools.magnitude(radius))
				temp+=4*mag*x[0]
				k+=1
			j+=1
		i=1
		while i<self.thing.size:
			self.E1= temp*(i**2)


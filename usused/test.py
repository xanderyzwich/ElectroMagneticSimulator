import numpy as np

x=np.arange(27)
x=x.reshape(3,3,3)
print x
print "and"

i=0
while i<3:
	j=0
	while j<3:
		k=0
		while k<3:
			print x[i,j,k]
			k+=1
		j+=1
	i+=1
print "end"




##	This block allows you to handle reading and writing nparrays as image'
import pylab as pl
import matplotlib.cm as cm
import numpy as np
import Image
import math

## this bit reads image into np.array
## picture of given name is returned np.array
## resulting array has values from 0 to 255 
## black is 0 and white is 255
def read(picture):
	im = Image.open(picture)
	im_grey = im.convert('L') # convert the image to *greyscale*
	im_array = np.array(im_grey)
	#pl.imshow(im_array, cmap=cm.Greys_r)
	#pl.show() 
	return im_array

##	this bit writes the array as an image
##	takes in np.array A, outputs image of given name
def write(A, picture):
	im = Image.fromarray(A)
	im.save(picture)

##	this is a fibonacci recursion for practice	
##	UNUSED
def fib(arg):
	if arg == 0:
		return 0
	elif arg == 1:
		return 1
	else:
		t1 = arg-1
		t2 = arg-2
		t1 = fib(t1)
		t2 = fib(t2)
		t = t1 + t2
		return t
		
##	this is a factorial recursion for practice
##	UNUSED
def fact(arg):
	if arg == 1:
		return 1
	else:
		t1 = arg - 1
		t2 = fact(t1)
		t3 = arg * t2
		return t3

##	this returns a 3D vector for the radius between two points
##	format of vector is [x,y,z]
def radv(v1,v2):
	v3=blank()
	v3[0]=v2[0]-v1[0]
	v3[1]=v2[1]-v1[1]
	v3[2]=v2[2]-v1[2]
	return v3

##	This returns the vector between to points in 3 space
##	used to create the R vector in field formula
def rad(x1,y1,z1,x2,y2,z2):
	v1=np.array([x1,y1,z1])
	v2=np.array([x2,y2,z2])
	v3=radv(v1,v2)
	return v3

##	this returns the magnitude of 3D vector
##	format of vector is [x,y,z]
##	used for radius magnitude in field formula
##	also used for creating unit vector
def magnitude(vector):
	mag=math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
	return mag

##	this returns a unit vector for a given vector 
##	used for unit radius in field formula
def unitrad(vector):
	x=vector[0]/magnitude(vector)
	y=vector[1]/magnitude(vector)
	z=vector[2]/magnitude(vector)
	return (x,y,z)

##	returns a zero vector of floats
##	used for vector initialization
def blank():
	return (0.0,0.0,0.0)
	
##	returns a ones vector
##	used for trouble shooting/practice
def one():
	return np.array([1,1,1])
	
##	returns constant portion of field formula
##	k= 1/(4*pi*E0)pyth
def k():
	E0=8.85*(10**-12)
	k=(4*math.pi*E0)**-1
	return k
	
##	returns smaller image from larger image
def truncate(a,sizeOut):
	v1=a.shape
	x1=v1[0]
	y1=v1[1]
	x2=y2=sizeOut
	offset=(x1-x2)/2
	b=np.zeros((x2,y2))
	i=0
	while i<sizeOut:
		j=0
		while j<sizeOut:
			b[i,j]=a[i+offset,j+offset]
			j+=1
		i+=1
	return b

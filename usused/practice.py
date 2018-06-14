#from helloworld import *
from simulation import *


#x=thing("check")
#x.out()

y=Simulation(50,50,50)
y.insert(0,0,0,50)
y.interrogate(0,0,1)
print y.space()

###	This block allows you to handle reading and writing nparrays as image'
#import pylab as pl
#import matplotlib.cm as cm
#import numpy as np
#import Image

### this bit reads image into np.array
#im = Image.open('your/image/path')
#im_grey = im.convert('L') # convert the image to *greyscale*
#im_array = np.array(im_grey)
#pl.imshow(im_array, cmap=cm.Greys_r)
#pl.show() 

###	this bit writes the array as an image
#im = Image.fromarray(A)
#im.save("your_file.jpeg")


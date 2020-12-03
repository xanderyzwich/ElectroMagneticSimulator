import numpy as np
from PIL import Image
import math


def pi():
    return math.pi


def E0():
    return 8.85e-12


def read(picture):
    """
    retrieve numpy.array from image file
    resulting array has values from 0 to 255
    black is 0 and white is 255
    :param picture: name of file to be read
    :return: numpy.array of image in file
    """
    im = Image.open(picture)
    im_grey = im.convert('L')  # convert the image to *greyscale*
    im_array = np.array(im_grey)
    return im_array


def write(A, picture):
    """
    Write numpy.array as an image
    :param A: file name
    :param picture: np.array to be write
    """
    im = Image.fromarray(A)
    im.save(picture)


def radv(v1, v2):
    """
    :param v1: first point
    :param v2: second point
    :return: 3D vector for the radius between two points formatted as [x,y,z]
    """
    v3 = blank()
    v3[0] = v2[0] - v1[0]
    v3[1] = v2[1] - v1[1]
    v3[2] = v2[2] - v1[2]
    return v3


def rad(x1, y1, z1, x2, y2, z2):
    """
    Create vector between two points in 3 space
    used to create the R vector in field formula
    :params x1, y1, z1: coords of first point
    :param x2. y2. z2: coords of second point
    :return: vector from first point to second point
    """
    v1 = np.array([x1, y1, z1])
    v2 = np.array([x2, y2, z2])
    v3 = radv(v1, v2)
    return v3


def magnitude(vector):
    """
    used for radius magnitude in field formula
    also used for creating unit vector
    :param vector: as [x,y,z]
    :return: magnitude of 3D vector
    """
    mag = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    return mag


def unitrad(vector):
    """
    used for unit radius in field formula
    :param vector:
    :return: unit vector of given vector
    """
    x = vector[0] / magnitude(vector)
    y = vector[1] / magnitude(vector)
    z = vector[2] / magnitude(vector)
    return np.array((x, y, z))


def blank():
    """
    used for vector initialization
    :return: a zero vector of floats
    """
    z = 0.0
    return np.array((z, z, z))


def field1(i, j, k, x1, y1, z, value):
    """
    field equation such that E=(Runit*q*c)/Rmag^2
    """
    c = float((4 * pi()() * E0()()) ** -1)
    Rvect = rad(i, j, k, x1, y1, z)  # Vector Radius
    Rmag = magnitude(Rvect)  # Magnitude Radius
    Runit = unitrad(Rvect)  # Unit vector Radius
    return (Runit * c * value) / (Rmag ** 2)


def field(q, R):
    """
    returns the field value given the Radius=r and charge=q
    """
    return q * ((4 * pi() * E0() * (R ** 2)) ** -1)


def fieldr(q, E):
    """
    returns the radius for the given charge=q and field value=E
    """
    return math.fabs(math.sqrt(q * (4 * pi() * E0() * E)))


def fieldy(q, E, x):
    """
    this only works for ideal and round situations
    :param q: charge
    :param E: field value
    :param x: distance
    :return: y value
    """
    return math.fabs((q * (4 * pi() * E0() * E)) - x ** 2)


def cosine(x, y, value):
    """

    :param x: x-component of unit vector
    :param y: y-component of unit vector
    :param value: vector magnitude
    :return: x value of the (x, y) vector scaled to value
    """
    return value * math.cos(math.atan(y / x))


def gety(x, r, a):
    return a + math.sqrt(r ** 2 - (x - a) ** 2)

from numpy import array, zeros, ones
from scipy import misc
from matplotlib import pyplot as plt
from math import sqrt, floor

import tools


class Layer(object):

    def __init__(self, size):
        self.size = size  # size of object in mm
        self.s1 = size + 1  # size of array including axes
        self.s2 = round(size / 2)  # distance left and right of axis
        self.small = self.s2 * (-1)  # negative end of array
        self.offset = self.s2 + 1  # axis location
        self.shape = (self.s1, self.s1)
        self.image = zeros(self.shape)

    def set(self, x, y, value):
        i = x + self.s2
        j = y + self.s2
        print(x, y), (i, j)
        self.image[i, j] = value

    def get(self, x, y):
        i = x + self.offset
        j = y + self.offset
        return self.image[i, j]

    def scale(self, value):
        self.image = (self.image) * value

    def mirror2(self, x, y, value):
        if value == 0:
            return
        x2 = -x
        self.set(x, y, value)
        self.set(x2, y, value)

    def mirror4(self, x, y, value):
        if value == 0:
            return
        y2 = -y
        self.mirror2(x, y, value)
        self.mirror2(x, y2, value)

    def mirror8(self, x, y, value):
        print("          call")
        if value == 0:
            return
        # creates mirror across x=y and x+y=self.s11
        self.mirror4(x, y, value)
        self.mirror4(y, x, value)

    def show(self):
        im = self.image * 255
        plt.imshow(im)
        plt.axis('off')
        plt.show()


class Wire(Layer):
    def __init__(self, size):
        super(Wire, self).__init__(size)
        self.square = 0
        self.draw()

    def set(self, x, y, value):
        super(Wire, self).set(x, y, value)

    def get(self, x, y):
        super(Wire, self).get(x, y)

    def scale(self, value):
        super(Wire, self).scale(value)

    def mirror8(self, x, y, value):
        super(Wire, self).mirror8(x, y, value)

    def mirror4(self, x, y, value):
        super(Wire, self).mirror4(x, y, value)

    def mirror2(self, x, y, value):
        super(Wire, self).mirror2(x, y, value)

    def show(self):
        super(Wire, self).show()

    def draw(self):
        self.set(self.offset, self.offset, 1)


class Box(Layer):
    def __init__(self, size):
        super(Box, self).__init__(size)
        self.square = 1
        self.draw()

    def draw(self):
        self.count = 0
        x = self.small
        while x < 0:
            self.mirror8(x, self.small, 1)
            self.count += 8
            x += 1
        self.mirror4(0, self.small, 1)
        self.count += 4

    def set(self, x, y, value):
        super(Box, self).set(x, y, value)

    def get(self, x, y):
        super(Box, self).get(x, y)

    def scale(self, value):
        super(Box, self).scale(value)

    def mirror8(self, x, y, value):
        super(Box, self).mirror8(x, y, value)

    def mirror4(self, x, y, value):
        super(Box, self).mirror4(x, y, value)

    def mirror2(self, x, y, value):
        super(Box, self).mirror2(x, y, value)

    def show(self):
        super(Box, self).show()


class Block(Layer):
    def __init__(self, size):
        super(Block, self).__init__(size)
        self.image = ones((size, size))
        self.size = size
        self.square = 1
        self.value = 1
        self.count = size ** 2

    # self.draw()
    def draw(self):
        self.count = 0
        x = self.small
        while x <= 0:
            y = self.small
            while y < x:
                if y == x and x != 0:
                    self.mirror4(x, y, 1)
                    self.count += 4
                elif y == 0:
                    self.set(x, x, 1)
                    self.count += 1
                else:
                    self.mirror8(x, y, 1)
                    self.count += 8
                y += 1
            x += 1

    def set(self, x, y, value):
        super(Block, self).set(x, y, value)

    def get(self, x, y):
        # super(Block, self).get(x,y)
        tools.field(x, y)  # this makes my code checker shutup
        return self.value

    def scale(self, value):
        super(Block, self).scale(value)
        self.value = self.value * value

    def mirror8(self, x, y, value):
        super(Block, self).mirror8(x, y, value)

    def mirror4(self, x, y, value):
        super(Block, self).mirror4(x, y, value)

    def mirror2(self, x, y, value):
        super(Block, self).mirror2(x, y, value)

    def show(self):
        super(Block, self).show()


class Tube(Layer):
    def __init__(self, size):
        super(Tube, self).__init__(size)
        self.square = 0
        self.draw()

    def set(self, x, y, value):
        super(Tube, self).set(x, y, value)

    def get(self, x, y):
        super(Tube, self).get(x, y)

    def scale(self, value):
        super(Tube, self).scale(value)

    def mirror8(self, x, y, value):
        super(Tube, self).mirror8(x, y, value)

    def mirror4(self, x, y, value):
        super(Tube, self).mirror4(x, y, value)

    def mirror2(self, x, y, value):
        super(Tube, self).mirror2(x, y, value)

    def show(self):
        super(Tube, self).show()

    def draw(self):
        r = self.s2
        self.count = 0
        x = (-1) * floor(sqrt(0.5 * (r ** 2)))
        while x <= 0:
            y = round(-sqrt(r ** 2 - x ** 2))
            self.mirror8(x, y, 1)
            self.count += 8
            x += 1
        self.mirror4(0, r, 1)
        self.count += 4


class Rod(Layer):
    def __init__(self, size):
        super(Rod, self).__init__(size)
        self.square = 0
        self.draw()

    def draw(self):
        r = self.s2
        self.count = 0
        x = (-1) * floor(sqrt(0.5 * (r ** 2)))
        while x <= 0:
            y = round(-sqrt(r ** 2 - x ** 2))
            while y <= x:
                if y == x and x != 0:
                    self.mirror4(x, y, 1)
                    self.count += 4
                elif y == 0:
                    self.set(x, y, 1)
                    self.count += 1
                else:
                    self.mirror8(x, y, 1)
                    self.count += 8

    def set(self, x, y, value):
        super(Rod, self).set(x, y, value)

    def get(self, x, y):
        super(Rod, self).get(x, y)

    def scale(self, value):
        super(Rod, self).scale(value)

    def mirror8(self, x, y, value):
        super(Rod, self).mirror8(x, y, value)

    def mirror4(self, x, y, value):
        super(Rod, self).mirror4(x, y, value)

    def mirror2(self, x, y, value):
        super(Rod, self).mirror2(x, y, value)

    def show(self):
        super(Rod, self).show()


class Plates(Layer):
    def __init__(self, size):
        super(Plates, self).__init__(size)
        self.draw()

    def draw(self):
        self.image[:, 0] = 1
        self.image[:, self.s1] = 1

    def set(self, x, y, value):
        super(Plates, self).set(x, y, value)

    def get(self, x, y):
        super(Plates, self).get(x, y)

    def scale(self, value):
        # super(Plates, self).scale(value)
        value = float(value / 2)
        self.image[:, 0] = -value
        self.image[:, self.s1] = value

    def mirror8(self, x, y, value):
        super(Plates, self).mirror8(x, y, value)

    def mirror4(self, x, y, value):
        super(Plates, self).mirror4(x, y, value)

    def mirror2(self, x, y, value):
        super(Plates, self).mirror2(x, y, value)

    def show(self):
        super(Plates, self).show()

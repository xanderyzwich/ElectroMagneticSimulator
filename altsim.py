from layers import *
# from layer import *
from numpy import array, zeros
import tools
from math import sqrt, floor


class Simulation:
    def __init__(self, image, charge=0, infinite=0, size=0.2):
        self.infinite = infinite
        self.image = image.lower()
        self.realSize = size
        self.size = size * 1e3
        self.transition = self.realSize * 10
        self.charge = charge
        self.thing = None

        ## create the charged object in 2D
        if image == 'wire':
            self.thing = Wire(self.size)
        elif image == 'box':
            self.thing = Box(self.size)
        elif image == 'block':
            self.thing = Block(self.size)
        elif image == 'tube':
            self.thing = Tube(self.size)
        elif image == 'rod':
            self.thing = Rod(self.size)
        elif image == 'plates':
            self.thing = Plates(self.size)
        else:
            self.thing = Block(self.size)

        # apply the proper charge to the object
        if self.charge == 0:
            electron = 1.6021765e-19
            self.charge = size * self.thing.count * electron
        if not self.infinite:
            self.thing.scale(self.charge)
        else:
            # for infinite "wire" the linear charge distribution
            # will be coulombs per meter
            # 1000 layers per meter
            self.thing.scale(self.charge * 1e-3)

    # self.start()
    def draw(self):
        self.thing.show()
        g = 50  # pixels per meter
        top = Layer(500)
        r = 1
        i = 1
        while r <= 250:
            x = top.s2 - r
            while x < top.s2:
                y = tools.gety(x, r, top.s2)
                top.mirror8(x, y, 255)
                x += 1
            r = floor(r * sqrt(10))
            i = i * 0.1
        top.show()
        q = top.space[:, top.s2]
        if self.infinite:
            i = 0
            side = Layer(500)
            while i < side.s1:
                side.space[:, i] = q
                i += 1
        else:
            side = top
        side.show()

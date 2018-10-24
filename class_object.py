class Area:
    def __init__(self,side):
        self.side=side
        print('Parameterized constructor is called with parameter ',side)
    def square(self,side):
        self.side=side
        print('Area of square of side',side,'is',side*side)
    def triangle(self,base,height):
        self.base=base
        self.height=height
        print('Area of Triange is ',0.5*base*height)
a1 = Area(4)
a1.square(5)
a1.triangle(4,12)

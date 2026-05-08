import math
class circle:
    def __init__(self, radio):
        self.radio = radio

    def get_area(self):
        area = math.pi * (math.pow(self.radio,2))
        print (area) 

circle1 = circle(2)
circle1.get_area()
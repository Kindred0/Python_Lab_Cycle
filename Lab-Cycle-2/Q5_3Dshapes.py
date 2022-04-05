from cmath import pi


class shapes_3D:
    def print_volume(self):
        print("Volume\t\t: ",self.volume)
    def print_area(self):
        print("Surface Area\t: ",self.area)

class cylinder(shapes_3D):
    def __init__(self):
        self.radius=int(input("Enter the radius of the cylinder\t: "))
        self.height=int(input("Enter the height of the cylinder\t: "))
        self.area=2*((pi*self.radius*self.height)+(pi*(self.radius**2)))
        self.volume=pi*(self.radius**2)*self.height

class spheare(shapes_3D):
    def __init__(self):
        self.radius=int(input("Enter the radius of the spheare\t: "))
        self.volume=((4/3)*pi*(self.radius**3))
        self.area=(4*pi*(self.radius**2))

c=cylinder()
c.print_area()
c.print_volume()
s=spheare()
s.print_area()
s.print_volume()
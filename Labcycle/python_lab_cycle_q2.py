
"""Program to read sides of two triangles  and find its area and contribution 
"""



def get_area():
  a=int(input("Enter side1\t= "))
  b=int(input("Enter side2\t= "))
  c=int(input("Enter side3\t= "))
  return a,b,c

def area_of_triangle():
    a,b,c=get_area()
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**.5
    return area

def Contribution(a,b):
    return (a/(a+b))*100

print("First Triangle : ")
area1=area_of_triangle()
print("Area\t= ",area1)
print("Second Triangle : ")
area2=area_of_triangle()
print("Area\t= ",area2)
print("Total area\t: ",area1+area2)
print("The contribution of the first triangle is\t= ",Contribution(area1,area2),"%")
print("The contribution of the second triangle is\t= ",Contribution(area2,area1),"%")
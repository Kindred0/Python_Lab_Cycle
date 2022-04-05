import random


class box:
    def __init__(self,a):
        if len(a)==3:
            self.length=a[0]
            self.breadth=a[1]
            self.height=a[2]
        elif len(a)==2:
            self.length=a[0]
            self.breadth=a[0]
            self.height=a[1]
        elif len(a)==1:
            self.length=a[0]
            self.breadth=a[0]
            self.height=a[0]
    def calc_area(self):
        self.area=2*(self.length*self.breadth+self.length*self.height+self.breadth*self.height)
        return self.area
    def calc_volume(self):
        self.volume=self.length*self.breadth*self.height
        return self.volume
    def display(self):
        print("Length\t: ",self.length)
        print("Breadth\t: ",self.breadth)
        print("Height\t: ",self.height)


N=int(input("Enter the number of boxes\t: "))
Ls=[]
for i in range(0,N):
    action=random.randint(1,3)
    var1=random.randint(1,200)
    var2=random.randint(1,200)
    var3=random.randint(1,200)
    if action==1:
        Ls.append(box([var1]))
    elif action==2:
        Ls.append(box([var1,var2]))
    elif action==3:
        Ls.append(box([var1,var2,var3]))
ratio=0
for i in Ls:
    if((i.calc_volume()/i.calc_area())>ratio):
        ratio=(i.calc_volume()/i.calc_area())
        N=i

print("The box with ")
N.display()
print("highest volume to area ratio of\t: ",ratio)



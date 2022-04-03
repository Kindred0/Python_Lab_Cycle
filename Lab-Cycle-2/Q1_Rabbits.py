


month=int(input("Enter the generation\t: "))
a=0
b=1
print("-----------------------------------------------")
print("|","Generation".center(20),"|","Pairs of Rabbits".center(20),"|")
print("|","1".center(20),"|","1".center(20),"|")
for i in range(1,month):
    temp=a
    a=b
    b=temp+b
    print("|",str(i+1).center(20),"|",str(b).center(20),"|")
print("-----------------------------------------------")
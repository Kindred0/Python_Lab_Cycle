from posixpath import split

#Read the string of numbers seperated by comma and converting them to list

numbers=input("Enter Numbers seperates by comma\t: ")
numbers=list(numbers.split(","))
N=[]
for i in numbers:
    N.append(int(i))
print(N)

#1)  Rotating the list by k amount to the left 

k=int(input("Enter the number of times to rotate the list\t: "))
for i in range(0,k):
    temp=N[-1]
    for j in range(1,len(N)):
        N[-j]=N[-(j+1)]
    N[0]=temp
print(N)

#2)  Converting the list to tuple

N=tuple(N)
print("List converted to Tuple")
print(N)

#3)  Deleting the duplicates and converting everything back to list again

N=set(N)
N=list(N)
print("Deleted duplicates from the list")
print(N)

#4)  List of f(x)=x^2-x

k=int(input("Enter a number\t: "))
M=[]
for i in range(1,k+1):
    M.append((k**2)-k)
print(M)

#5)  Sporting the two lists and merging them together

N.sort()
M.sort() 
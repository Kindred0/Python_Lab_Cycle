#Program to check if a number is happy number and to print all happy numbers in a range


def sum_square(number):
  number=str(number)
  A=[]
  for i in number:
    A.append(int(i))
  sum=0
  for i in range(0,len(A)):
    sum=sum+(A[i]*A[i])
  return sum

def is_happy(number):
  happy=0
  for i in range(0,100):
    if number!=1:
      number=sum_square(number)
    else:
      return True
  return False


number=int(input("Enter a number\t: "))
if is_happy(number):
  print(number,"\t: The number is happy")
else:
  print(number,"\t: The numeber is sad")
start=int(input("Enter the starting point\t: "))
stop=int(input("Enter the stopping point\t: "))
print("Happy numbers in the range (",start,",",stop,")")
for i in range(start,stop+1):
  if is_happy(i):
    print(i)
N=int(input("Enter N\t: "))
print("Happy numbers in range(",0,",",N,")")
for i in range(0,N+1):
  if is_happy(i):
    print(i)
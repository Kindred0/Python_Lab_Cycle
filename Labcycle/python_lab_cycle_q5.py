# Program to print all substrings of a string with certain constraints and to find the palindrome of the substrings



def get_substring(str1):
  A=[]
  i=0
  while i<len(str1)+1:
    j=i+1
    while j<len(str1)+1:
      sub_string=str(str1[i:j])
      A.append(sub_string)
      j=j+1
    i=i+1
  return A

def check_length(str1,length):
  B=[]
  list1=get_substring(str1)
  for i in list1:
    if len(i)==length:
      B.append(i)
  return B

def check_distinct(str1,number):
  B=[]
  list1=get_substring(str1)
  for i in list1:
    set1=set(i)
    if len(set1)==number:
      B.append(i)
  return B

def palindrome(str1):
  B=[]
  list1=get_substring(str1)
  for i in list1:
    B.append(i[::-1])
  return B

str1=input("\nEnter a string\t: ")
A=get_substring(str1)
print("\nAll the substrings\t: ")
print(A)
L=int(input("\nEnter the length of the substring\t: "))
print("\nAll the sustrings of length ",L)
print(check_length(str1,L))
D=int(input("\nEnter the number of distinct elements\t: "))
print("\nAll the substrings with distinct elements\t: ",D)
print(check_distinct(str1,D))

L=int(input("\nEnter the length of the substring\t: "))
D=int(input("\nEnter the number of distinct elements\t: "))
print("Sunstrings with distinct elements",D,"And maximum length of",L)
B=[]
A=check_distinct(str1,D)
for i in A:
  if len(i)==L:
    B.append(i)
print(B)
print("\nAll the substring palindroms\t: ")
print(palindrome(str1))

"""Devolop a pogram read a four digit number and find its 
sum of digits
reverse
differnce between the product of even and odd digits numbers
"""

a=int(input("Enter a number\t: "))
digit1=a%10
a=a//10
digit2=a%10
a=a//10
digit3=a%10
a=a//10
digit4=a%10
a=a//10
sum=digit1+digit2+digit3+digit4
reverse=digit1*1000+digit2*100+digit3*10+digit4
diff=(digit3*digit1)-(digit4*digit2)
print("Sum of the digits is\t= ",sum)
print("Reverse of thenumber is\t= ",reverse)
print("Difference between the product of odd digits and product of even digits is\t= ",diff)

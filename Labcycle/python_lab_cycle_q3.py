
#Program to find the net salary of an employee from the given details

def Net_Salary(basic_pay,DA,HRA,MA,PT,PF,IT):
  DA=basic_pay*DA/100
  HRA=basic_pay*HRA/100
  PF=basic_pay*PF/100
  IT=basic_pay*IT/100
  GS=basic_pay+DA+HRA+MA
  D=PT+PF+IT
  return GS-D


name=str(input("Employee Name\t: "))
code=int(input("Employer code\t: "))
basic_pay=int(input("Basic pay\t: "))
if basic_pay<10000:
  DA=5
  HRA=2.5
  MA=200
  PT=20
  PF=8
  IT=0
elif basic_pay<30000:
  DA=7.5
  HRA=5
  MA=2500
  PT=60
  PF=8
  IT=0
elif basic_pay<50000:
  DA=11
  HRA=7.5
  MA=5000
  PT=60
  PF=11
  IT=11
else:
  DA=25
  HRA=11
  MA=7000
  PT=80
  PF=12
  IT=20

print("Employer Name\t: ",name)
print("Employer Code\t: ",code)
print("Salary\t\t: ",Net_Salary(basic_pay,DA,HRA,MA,PT,PF,IT))
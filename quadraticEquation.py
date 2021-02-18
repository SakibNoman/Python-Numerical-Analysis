
#importing modules
import math
import cmath

#Taking input and converting to float
a = float(input())
b = float(input())
c = float(input())

#checking if there any valid solution and finding the solution
if a==0:
  print("The equation is not a valid quadratic equation.")
else:
  if b*b < 4*a*c:
    d = b**2-4*a*c
    x1 = (-b-cmath.sqrt(d))/2*a
    x2 = (-b+cmath.sqrt(d))/2*a
    print(x1,x2)
  else:
    d = b**2-4*a*c
    x1 = (-b-math.sqrt(d))/2*a
    x2 = (-b+math.sqrt(d))/2*a
    print(x1,x2)

#Thank you
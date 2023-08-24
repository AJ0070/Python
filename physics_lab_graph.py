

x1=float(input("Enter x1:"))
x2=float(input("Enter x2:"))
x3=float(input("Enter x3:"))
x4=float(input("Enter x4:"))
x5=float(input("Enter x5:"))
x6=float(input("Enter x6:"))
x7=float(input("Enter x7:"))
x_sum = x1+x2+x3+x4+x5+x6+x7


y1=float(input("Enter y1:"))
y2=float(input("Enter y2:"))
y3=float(input("Enter y3:"))
y4=float(input("Enter y4:"))
y5=float(input("Enter y5:"))
y6=float(input("Enter y6:"))
y7=float(input("Enter y7:"))
y_sum=y1+y2+y3+y4+y5+y6+y7

multiplication_1= x1*y1+x2*y2+x3*y3+x4*y4+x5*y5+x6*y6+x7*y7
mu=multiplication_1

sum_xsq= x1*x1+x2*x2+x3*x3+x4*x4+x5*x5+x6*x6+x7*x7
xs=sum_xsq

sum_xwsq=x_sum**2
xw= sum_xwsq

if x5!=0:
    n=5


  

if x6==0:
    n=5
else :
    n=6


if x7==0:
    n=6
else :
    n=7    

u = n*mu - x_sum*y_sum
v=n * sum_xsq - sum_xwsq

m = u /v 

z=y_sum - m * x_sum

c =  z/ n

x = float(input("Enter the value of x: "))

y = m * x + c

print(y)
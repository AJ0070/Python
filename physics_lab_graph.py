n = int(input("Enter the number of data points: "))
x_values = []
y_values = []

for i in range(n):
    x = float(input(f"Enter x{i+1}: "))
    y = float(input(f"Enter y{i+1}: "))
    x_values.append(x)
    y_values.append(y)

x_sum = sum(_values)
y_sum = sum(y_values)

multiplication_1 = sum(x * y for x, y in zip(x_values, y_values))
sum_xsq = sum(x ** 2 for x in x_values)
sum_xwsq = x_sum ** 2

u = n * multiplication_1 - x_sum * y_sum
v = n * sum_xsq - sum_xwsq

if x_values[4] != 0:
    n = 5
elif x_values[5] != 0:
    n = 6
else:
    n = 7

m = u / v

z = y_sum - m * x_sum
c = z / n

x = float(input("Enter the value of x: "))
y = m * x + c

print(f"The calculated y value for x={x} is {y}")

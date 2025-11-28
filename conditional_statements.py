# Q1. Predict the Output
x = 10
y = 5

if x > y:
    x = x + y
else:
    y = y + x

print("Q1 output :", x, y)

# and the output is x = 15 and y = 5





# Q2. Slightly harder (with elif)
a = 7
b = 12

if a > b:
    a = a - b
elif b > a:
    b = b - a
else:
    a = a + b

print("Q2 output :", a, b)

# and the output is a = 7 and b = 5
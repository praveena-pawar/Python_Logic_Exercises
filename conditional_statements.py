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





# Q3. Conditional + Logical Operators
x = 8
y = 3
z = 10

if x > y and z > x:
    x = x + z
else:
    y = y + z

print("Q3 output :", x, y, z)

# and the output x = 18 , y = 3 and z = 10






# Q4. Conditional + Logical OR
a = 5
b = 10
c = 7

if a > b or c < a:
    a = a + c
else:
    b = b + c

print("Q4 output :", a, b, c)

#  and the output a = 5, b = 17, c = 7
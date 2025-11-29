# Q1: Conditional + Nested If 
# This one combines if-else, nested if, and logical operators.
a = 8
b = 5
c = 12

if a < c:
    if b > a:
        b = b + a
    else:
        a = a + c
else:
    c = c + b

print("Q1 output :", a, b, c)

# and the output a = 20, b = 5 and c = 12








# Q2. Tricky Conditional + Logical Operators + Nested If
x = 7
y = 10
z = 5

if x + y > z * 3:
    if y - x < z:
        x = x + y
    else:
        y = y + z
else:
    z = z + x

print("Q2 output :", x, y, z)

# and the ouptut x = 17, y = 10, z = 5
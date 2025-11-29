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
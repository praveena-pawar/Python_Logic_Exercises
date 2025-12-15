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






# Q3. Predict the Output
a = 10
b = 5
c = 20

if a > b and (c < a or b == 5):
    if c > a + b:
        print("X")
    elif c == a + b:
        print("Y")
    else:
        print("Z")
else:
    print("No Match")


# and the output X




# Q4. Predict the Output
x = 10
y = 5
z = 0

if x > y and not (y > z):
    if x - y == z:
        print("A")
    else:
        print("B")
else:
    print("C")

#  and the output C 





# Q5. Predict the Output
a = 7
b = 3
c = 9

if a < b or c > a:
    if not (b * 3 == a):
        print("X")
    elif c - a > b:
        print("Y")
    else:
        print("Z")
else:
    print("W")


# and the output X






# Q6. Predict the Output
age = 20
has_id = True
is_student = False

if age >= 18:
    if has_id and not is_student:
        if age % 2 == 0:
            print("Allowed")
        else:
            print("Check Again")
    else:
        print("ID Required")
else:
    print("Not Allowed")

# and the output Allowed




# Q7. Predict the Output
a = 10
b = 5
c = 20

if a > b:
    if b > c:
        print("A")
    else:
        if a + b == c:
            print("B")
        else:
            print("C")
else:
    print("D")

# and the output for Q7 : c






# Q8. Predict the Output
x = 7

if x > 5:
    if x % 2 == 0:
        print("Even")
    else:
        if x > 10:
            print("Big Odd")
        else:
            if x == 7:
                print("Lucky")
            else:
                print("Odd")
else:
    print("Small")

# and the output for Q8 : "Lucky"






# Q9. Predict the Output
a = 3
b = 6
c = 9

if a + b > c:
    print("X")
else:
    if b * a == c:
        if c - b == a:
            print("Y")
        else:
            print("Z")
    else:
        print("W")

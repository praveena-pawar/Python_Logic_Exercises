# ✅ DAY-1: Logic Building Exercises

# Q1. Predict the output
x = 5
y = 2

x = x + y      # step 1
y = x - y      # step 2
x = x - y      # step 3

print("Q1 output:", x, y)

# and the out put is x = 2 and y = 5



# Q2. Predict the output
a = 10
b = 3

a = a * b      # step 1
b = a // b     # step 2
a = a // b     # step 3

print("Q2 output:", a, b)

# and the out put is a = 3 and b = 10






# Q3. Predict the Output
x = 4
y = 6
z = 2

x = x + y      # step 1
y = y + z      # step 2
z = x - y      # step 3
x = z + y      # step 4


print("Q3 output :", x, y, z)

# and the output is x = 10, y = 8, z = 2





# Q4. Predict the Output (slightly harder now)
a = 5
b = 12
c = 3

a = a * 2        # step 1
b = b - a        # step 2
c = c + b        # step 3
a = a + c        # step 4
b = a - c        # step 5

print("Q4 output :", a, b, c)

# and the output is a = 15 , b = 10 and c = 5





# Q5. Predict the Output (Now slightly more tricky — involves order of updates)
x = 8
y = 3
z = 4

x = x - y        # step 1
y = y * z        # step 2
z = x + y        # step 3
y = z - x        # step 4
x = x + y + z    # step 5

print("Q5 output :", x, y, z)

# and the output is x = 34, y = 12 and z = 17 





# Q6. Predict the Output (This is the toughest so far — but you can do it!)
a = 7
b = 2
c = 5
d = 3

a = a + b        # step 1
b = b + c        # step 2
c = c + d        # step 3
d = a + c        # step 4
a = d - b        # step 5

print("Q6 output :", a, b, c, d)

# and the output a = 10, b = 7, c = 8 and d = 17
 



# Q7. Predict the Output (Very Tricky)
x = 3
y = 9
z = 4

x = y - x        # step 1
y = x + z        # step 2
z = y - z        # step 3
x = x + y + z    # step 4
y = x - z        # step 5

print("Q7 output :",x, y, z)

# and the output is x = 22, y = 16 and z = 6






# Q8. Hardest Logic Update So Far
a = 4
b = 7
c = 2
d = 5

a = b + c        # step 1
b = a - d        # step 2
c = b + d        # step 3
d = a + b + c    # step 4
a = d - c        # step 5

print("Q8 output :", a, b, c, d)

#and the output is a = 13, b = 4 , c = 9 and d = 22




# Q9. Most Tricky
m = 2
n = m + 5
o = n * m

m = o - n
n = m + o
o = n - m

m = o + n - m
print("Q9 output :", m, n, o)

# and the output is m = 28, n = 21 and o = 14





# Q10. Predict the Output (Very Tricky)
a = 6
b = a + 2
c = b - a

a = b * c
b = a + c
c = b - a

b = c + b
print("Q10 output :", a, b, c)

# and the output a = 16, b = 20 and c = 2 

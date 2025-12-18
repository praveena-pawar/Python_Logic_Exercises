# Q1. Nested Loop Predict the Output    
total = 0

for i in range(1, 4):      # i = 1,2,3
    for j in range(1, 3):  # j = 1,2
        total += i * j

print("Q1 output :", total)

#and the output total = 18




# Q2. Nested Loops with If Condition
total = 0

for i in range(1, 4):       # i = 1,2,3
    for j in range(1, 4):   # j = 1,2,3
        if (i + j) % 2 == 0:
            total += i * j
        else:
            total -= (i + j)

print("Q2 output :", total)

# and the output total 4





# Q3 — Loops + Nested If + Logical Operators
x = 2
y = 3
total = 0

for i in range(1, 4):       # i = 1,2,3
    for j in range(1, 4):   # j = 1,2,3
        if (i * j) % 2 == 0:
            total += i + j
        else:
            total -= i

print("Q3 output :", total)

# and the output total 12





# Q4 — Nested Loops with If Condition
total = 0

for i in range(1, 4):       # i = 1,2,3
    for j in range(1, 4):   # j = 1,2,3
        if (i + j) % 2 == 0:
            total += i * j
        else:
            total -= (i + j)

print("Q4 output :", total)

# and the output 4




# Q5 — Loops + Nested If + Logical Operators
x = 2
y = 3
total = 0

for i in range(1, 4):       # i = 1,2,3
    for j in range(1, 4):   # j = 1,2,3
        if (i * j) % 2 == 0:
            total += i + j
        else:
            total -= i

print("Q5 output :", total)

# and the output 12





# Q6 — Loops + Nested If + Logical Operators
total = 1
for i in range(1, 5):
    for j in range(i, 0, -1):
        if (i + j) % 2 == 0:
            total *= (i + j)
        else:
            total -= (i - j)
print("Q6 output :", total)

# and the output 7863





# Q7 — Loops + Nested If + Logical Operators
total = 1
for i in range(2, 6):
    for j in range(1, i):
        if j == 1 or j == i-1:
            total *= (i - j)
        else:
            total += (i + j)
print("Q7 output :", total)

# and the output 63





# Q8 — Loops + Nested If + Logical Operators
s = 10
for i in range(3, 7):
    for j in range(2, i):
        if (i * j) % 3 == 0:
            s += i - j
        elif (i + j) % 4 == 0:
            s -= i
        else:
            s += j
print("Q8 output:", s)

# and the output 32





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

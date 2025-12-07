    # Predict the Output

# Q1 — Simple Star Pattern
for i in range(1, 4):
    for j in range(1, i+1):
        print("*", end="")
    print()

# Q1 output
# *
# **
# ***




# Q2 — Right-Angled Number Pattern
for i in range(1, 5):          # i = 1,2,3,4
    for j in range(1, i+1):     # j = 1 to i
        print(j, end="")
    print()

# Q2 output 
# 1
# 12
# 123
# 1234
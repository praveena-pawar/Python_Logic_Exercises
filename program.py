# Q1. write a python program which accepts a number and prints its prime factors  
num = int(input("Enter a number : "))
is_prime = True
for i in range(2, int(num ** 0.5)+1):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num > 1 :
    print(f'{num} is a prime number')
else : 
    print(f'{num} is not a prime number')








# Q2. write a python program that checks whether a give password id valid. An acceptable password :
# a) should have minimum 8 characters
# b) must have at least one digit and one special character
# c) must contain at least one alphabet which is in upper case
pwd = input("Enter password: ")

if (len(pwd) >= 8 and 
    any(ch.isdigit() for ch in pwd) and
    any(ch.isupper() for ch in pwd) and
    any(ch in "!@#$%^&*()_+-={}[]|:;<>,.?/~`" for ch in pwd)):
    print("Valid password")
else:
    print("Invalid password")






# Q3. write a program that creates a list and performs the following operations on the list
# a) mean, median and mode
# # b) maximum and minimum values in the list
# c) sort the list
# d) Remove the duplicate values from the list
from statistics import mean, median, mode
lst = [10, 20, 10, 40, 30, 20, 10]
print("List:", lst)
print("mean:", mean(lst))
print("median:", median(lst))
print("mode:", mode(lst))
print("min:", min(lst))
print("max", max(lst))

sorted_list = sorted(lst)
print("soretd list:", sorted_list)

unque_list = list(set(lst)) 
print("unique list:", unque_list)





# Q4. create a dictionary with student name(minimum 5) as keys and list a list of (subject, marks) tuples as values .
# display student details along with total marks and percentage of each student.
students = {
    "Ravi": [("Math", 85), ("Science", 78), ("English", 90)],
    "Sneha": [("Math", 92), ("Science", 88), ("English", 81)],
    "Karan": [("Math", 76), ("Science", 70), ("English", 65)],
    "Meera": [("Math", 89), ("Science", 95), ("English", 92)],
    "Ajay": [("Math", 60), ("Science", 55), ("English", 72)]
}
for name, marks in students.items():
    total = sum(marks for subjects, marks in marks)
    percent = total / len(marks)
    print(f"\n{name}'s total marks :{total}, percentage :{percent}%")






# Q5. implement Depth-First search (DFS) on small program
# Graph represented as a dictionary (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()   # To keep track of visited nodes

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(neighbour)

# Starting DFS from node 'A'
print("DFS Traversal:")
dfs('A')

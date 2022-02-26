# Ques1

def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)


n = int(input())
TowerOfHanoi(n, 'A', 'B', 'C')

# Ques2 -------

# Iterative
def fact(n):
    if(n <= 1):
        return 1
    return n * fact(n - 1)

n = int(input())
for i in range(n):
    for c in range(n - i + 1):
        print(end=" ")
    for j in range(i + 1):
        print(fact(i) // (fact(j) * fact(i - j)), end=" ")
    print()

# Recursive

def Pascal(n, originalength):
    if n == 0:
        return
    Pascal(n-1, originalength)
    print(" " * (originalength - n), end='')
    start = 1
    for i in range(1, n+1):
        print(start, end=" ")
        start = start * (n - i) // i
    print()
    
n = int(input())
Pascal(n, n)


# Ques 3 -------------

a = int(input())
b = int(input())
Quotient, Remainder = divmod(a, b)

# Part_1-----
print(callable(Quotient))
print(callable(Remainder))

# Part_2----
t = divmod(a, b)
if(t == (0, 0)):
    print("YES\n")
else:
    print("NO\n")
    
# Part_3-----
NewList = [Quotient + 4, Remainder + 4, Remainder + 5,
           Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]
result = []
for i in range(len(NewList)):
    if NewList[i] > 4:
        result.append(NewList[i])
print(f"Filtered out numbers that are greater than 4 are : {result}")

# Part_4-----
Set = set(result)
print("Set:", Set)

# Part_5-----
immutableSet = frozenset(Set)  # frozen Set is used to make the set immutable
print("Immutable set is :", immutableSet)

# Part_6-----
print("Hash value of the max value from the above set:", hash(max(immutableSet)))


# Ques 4 ---------

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __del__(self):
        print("Object destroyed")

obj = Student("Ankur", 21103028)
print(obj.name)
print(obj.roll)
del obj

# Ques 5 -----------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

Employee_1 = Employee("Mehak", 40000)
Employee_2 = Employee("Ashok", 50000)
Employee_3 = Employee("Viren", 60000)

# Part_1
Employee_1.salary = 70000
print(f"The updated salary of {Employee_1.name} is {Employee_1.salary} ")

# Part_2
del Employee_3
print("Record of Viren deleted")

# Ques 6---------

def make_list(s):
    li = []
    for i in range(len(s)):
        li.append(s[i])
    li.sort()
    return li
    
s = str(input())
s = s.lower()  # So that we convert the name to lowercase letters
y = str(input())
y = y.lower()  # So that we convert the name to lowercase letters
s = make_list(s)
y = make_list(y)
if s == y:
    print("Nice")
else:
    print("Fake")

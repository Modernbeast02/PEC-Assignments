# Ques1
s = str(input("Enter the string: "))
dict = {}
if s.count(" ") == 0:  # meaning its a single word and we have to count the occurances of characters
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
else:
    b = s.split(" ")
    for i in b:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)


# Ques 2

def Check_If_Leap_Year(Year):  # To check if the year is a leap year
    if(Year % 4 != 0):
        return False
    if(Year % 100 == 0):
        if(Year % 400 != 0):
            return False
    return True


Date = int(input("Enter the date: "))
Month = int(input("Enter the month: "))
Year = int(input("Enter the year: "))
Extra_Day_Months = [1, 3, 5, 7, 8, 10, 12]
if(Date < 28 or Date == 29):
    print("Next Date is:", Date + 1, "/", Month, "/", Year)
elif Date == 28:
    if Month != 2:
        print("Next Date is:", Date + 1, "/", Month, "/", Year)
    else:
        if Check_If_Leap_Year(Year):
            print("Next Date is:", Date + 1, "/", Month, "/", Year)
        else:
            print("Next Date is:", 1, "/", "03", "/", Year)
else:
    if Date == 31:
        if(Month == 12):
            print("Next Date is:", 1, "/", "01", "/", Year + 1)
        else:
            print("Next Date is:", 1, "/", Month + 1, "/", Year)
    else:
        if Month in Extra_Day_Months:
            print("Next Date is:", Date + 1, "/", Month, "/", Year)
        else:
            print("Next Date is:", 1, "/", Month + 1, "/", Year)

# Ques 3
n = int(input("Enter total numbers to be added to list: "))
li = []
for i in range(n):
    x = int(input())
    li.append((x, x * x))
print(li)

# Ques 4
grade = int(input("Enter Grade: "))
if grade < 4 or grade > 10:
    print("Error")
else:
    if(grade == 4):
        Grade = "D"
        Message = "Poor"
    if(grade == 5):
        Grade = "C"
        Message = "Below Average"
    if(grade == 6):
        Grade = "C+"
        Message = "Average"
    if(grade == 7):
        Grade = "B"
        Message = "Good"
    if(grade == 8):
        Grade = "B+"
        Message = "Very Good"
    if(grade == 9):
        Grade = "A"
        Message = "Excellent"
    if(grade == 10):
        Grade = "A+"
        Message = "Outstanding"

print("Your Grade is", Grade, "and", Message, "Performance")


# Ques 5
j = 13
for i in range(0, 6):
    for k in range(i):
        print(" ", end="")
    j = j - 2
    for l in range(j):
        print(chr(l + 65), end="")
    print(" ")

# Ques 6
dict = {}
while(True):
    s = str(input("Do you want to enter? "))
    if s == 'N' or s == "n":
        break
    else:
        Sid = int(input("Enter SID: "))
        Name = str(input("Enter name: "))
        dict[Sid] = Name
# Part A
print("Part A", dict)
# Part B
Sorted_Student_Names = sorted(dict.items(), key=lambda x: x[1])
print("Part B", Sorted_Student_Names)
# Part C
Sorted_SID = sorted(dict.items(), key=lambda x: x[0])
print("Part C", Sorted_SID)
# Part D
sid = int(input("Enter SID to search: "))
print("Part d ", dict[sid])

# Ques 7
n = int(input("Enter number for fibonacci"))
prev = 0
curr = 1
sum = 0
if n >= 1:
    print(prev)
if n >= 2:
    print(curr)
    sum = 1

for i in range(3, n + 1):  # Time Complexity O(N), Space Complexity O(1)
    print(prev + curr)
    sum = sum + prev + curr
    temp = prev + curr
    prev = curr
    curr = temp
print("average is :", sum / n)


# Ques 8
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# Part A
Set_Union = Set1
Set_Union.union(Set2)
Set_Intersection = Set1.intersection(Set2)
Set_Union = Set_Union - Set_Intersection
print("Part A", Set_Union)

# Part B
Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - \
    Set2.intersection(Set3) - Set3.intersection(Set1)
Part_B_Set.union(Set1.intersection(Set2.intersection(Set3)))
print("Part B", Part_B_Set)

# Part C
PartC_Set = set()
for i in Set1:
    if i in Set2 and i not in Set3:
        PartC_Set.add(i)
    elif i in Set3 and i not in Set2:
        PartC_Set.add(i)
for i in Set2:
    if i in Set1 and i not in Set3:
        PartC_Set.add(i)
    elif i in Set3 and i not in Set2:
        PartC_Set.add(i)
for i in Set3:
    if i in Set2 and i not in Set1:
        PartC_Set.add(i)
    elif i in Set1 and i not in Set2:
        PartC_Set.add(i)

print("Part C", PartC_Set)

# Part D
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("Part D", Part_D_Set)

# Part E
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("Part E", Part_E_Set)

string = str("Python is a case sensitive language")
print(len(string))
string = string[::-1]  # reverse the string


# Ques2

Name = str("ABC")
SID = 21103028
CGPA = 9.9
Department = str("CSE")
print("Hey,", Name, "Here!")
print("My SID is", SID)
print("I am from", Department, "and my CGPA is ", CGPA)

# Ques 3

a = 56
b = 10
print(a & b)
print(a | b)
print(a ^ b)
# D part
a = a << 2
b = b << 2
# E part
a = a >> 2
b = b >> 4

# Ques 4
list = []
for i in range(3):
    x = int(input())
    list.append(x)
list.sort()       #largest number will reach the last index of list
print(list[-1])

# Ques 5

string = str(input())
flag = False
for i in range(len(string) - 3):
    if(string[i: i + 4] == "name"):  #checking every substring of size 4
        flag = True
if (flag == True):
    print("YES")
else:
    print("NO\n")

# Ques 6

list = []
for i in range(3):
    x = int(input())
    list.append(x)
list.sort()   #sorting the list
if(list[0] + list[1] < list[2]):  #if 2 small numbers sum is greater than largest side sum, then we can form triangle
    print("NO\n")
else:
    print("YES\n")



# Ques1
string = str("Python is a case sensitive language")
s = string
print("Length of original string is", len(string))
string = string[::-1]  # reverse the string
print("Reversed string --", string)
new_string = s[10:26]
new_string.replace("a case sensitive", "object oriented")
print("Index of 'a' in original string is", s.find('a'))
print("Original String after removing whitespace --", s.replace(" ", ""))


# Ques2
Name = "Ankur Gupta"
SID = 21103028
CGPA = 10
Department = "CSE"
print("Hey, %s Here!" % Name)
print("My SID is %d" % SID)
print("I am from %s and my CGPA is %d" % (Department, CGPA))


# Ques 3
a = 56
b = 10
print(a & b)
print(a | b)
print(a ^ b)
# D part
print(a << 2)
print(b << 2)
# E part
print(a >> 2)
print(b >> 4)


# Ques 4
list = []
for i in range(3):
    x = int(input("Enter the number: "))
    list.append(x)
list.sort()
# the last index will contain the maximum value
print("Max number is", list[-1])


# Ques 5
string = str(input("Enter the string: "))
if("name" in string):
    print("Yes\n")
else:
    print("No\n")


# Ques 6
list = []
for i in range(3):
    x = int(input("Enter Triangle Side Length: "))
    list.append(x)
list.sort()
if(list[0] + list[1] < list[2]):
    print("No\n")
else:
    print("Yes\n")

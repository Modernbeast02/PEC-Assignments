# Ques1
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))
num4 = num1 + num2 + num3
average = num4 / 3
print("Average is : ", average)

# Ques2
Gross_Income = int(input("Enter the Gross Income : "))
Dependent = int(input("Enter Dependent : "))
Standard_deduction = 10000
Dependent_deduction_amount = Dependent * 3000
Taxable_Income = Gross_Income - Standard_deduction - Dependent_deduction_amount
Tax = float((20/100) * (Taxable_Income))  # Tax is 20% of Taxable_Income
print("Your income tax : ", Tax)


# Ques3
Student_Details = []
SID = int(input("Enter SID: "))
Name = str(input("Enter Name: "))
Gender = str(input("Enter Gender: "))
Course_Name = str(input("Enter Course Name: "))
CGPA = float(input("Enter CGPA: "))
Student_Details.append(SID)
Student_Details.append(Name)
Student_Details.append(Gender)
Student_Details.append(Course_Name)
Student_Details.append(CGPA)
print("Student Details :", Student_Details)


# # Ques4
Marks = []
for i in range(5):
    print("Enter Marks", i + 1, ": ", end="")
    x = int(input())
    Marks.append(x)
Marks.sort()  # Sorting the marks list
print("Sorted Order Of Marks : ", Marks)


# # Ques 5
Student_Details = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Student_Details.remove('Black')
print("Part a :", Student_Details)
Student_Details[3] = 'Purple'  # Replacing Pink with Purple
print("Part b :", Student_Details)

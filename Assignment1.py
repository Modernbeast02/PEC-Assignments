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
Color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
List_for_partA = Color
List_for_partA.remove('Black')
print("Part a :", List_for_partA)
Color[3:5] = ['Purple']  # Replacing Black and Pink with Purple
print("Part b :", Color)

# -----------------------------------------------------------------------------------------

Output:
# Ques1
Enter First Number : 5Output:
Enter First Number : 5
Enter Second Number : 10
Enter Third Number : 15
Average is :  10.0

 
# Ques2
Enter the Gross Income : 1000000
Enter Dependent : 2
Your income tax :  196800.0
    
# Ques3
Enter SID: 21103028
Enter Name: Ankur
Enter Gender: Male
Enter Course Name: Introduction to Computing
Enter CGPA: 9.90
Student Details : [21103028, 'Ankur', 'Male', 'Introduction to Computing', 9.9]

# Ques4
Enter Marks 1 : 90 
Enter Marks 2 : 99
Enter Marks 3 : 95
Enter Marks 4 : 98 
Enter Marks 5 : 93
Sorted Order Of Marks :  [90, 93, 95, 98, 99]
    
# Ques5
Part a : ['Red', 'Green', 'White', 'Pink', 'Yellow']
Part b : ['Red', 'Green', 'White', 'Purple', 'Yellow']


    

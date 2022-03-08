# Ques1
# GST Rate Calculator
from tkinter import *

def calc():
    global gst
    if(netprice.get().isdecimal() == False):
        gst.set("Invalid Input")  # If the Output Does Not Contain Numbers
        g.update() 
    else:
        gstrate = ((float(netprice.get()) - float(originalcost.get()))
                   * 100) / float(originalcost.get())
        if (gstrate >= 0):
            gst.set(gstrate)
            g.update()
        else:
            gst.set("Invalid Input")
            g.update()

root = Tk()
root.geometry("300x200")
root.maxsize(300, 200)
root.minsize(300, 200)
lab1 = Label(text="GST Tax Finder Calculator", font="comicsans 10 bold")
lab1.grid(row=0, column=1)
netprice = StringVar()
originalcost = StringVar()
gst = StringVar()
np1 = Label(text="Net Price:")
np1.grid(row=1, column=0)
# Creating Entry Column
e1 = Entry(root, textvariable=netprice, font="comicsans 10 bold")
e1.grid(row=1, column=1)
# Creating Label
oc1 = Label(text="Original Cost:")
oc1.grid(row=2, column=0)  # Packing The Label in form of grid
oc = Entry(root, textvariable=originalcost,
           font="comicsans 10 bold")  # Creating Entry
oc.grid(row=2, column=1)  # Packing The Label in form of Grid
# Creating a button named Calculate GST Rate
cal = Button(text="Calculate GST Rate", command=calc)
cal.grid(row=3, column=1)  # Packing The Label in form of grid
g1 = Label(text="GST Rate:")  # Creating Label
g1.grid(row=4, column=0)  # Packing The Label in form of grid
g = Entry(root, textvariable=gst, font="comicsans 10 bold")  # Creating Label
g.grid(row=4, column=1)  # Packing The Label in form of grid
root.mainloop()


# Ques2
# Calendar
from tkinter import *
from calendar import calendar
import calendar

root = Tk()


def cal1():
    global year
    new = Tk()
    new.geometry("600x700")
    l1 = Label(new, text=(calendar.calendar(int(year.get()))),
               font="Consolas 10 bold")
    l1.grid(row=0, column=0, padx=30)
    new.mainloop()

root.geometry("400x300")
heading = Label(text="Calendar", font="comicsans 20 bold")
heading.place(x=140, y=1)  # Using place to pack the label
year1 = Label(text="Enter Year: ")
year1.place(x=20, y=50)  # Using place to pack the label
year = StringVar()
e2 = Entry(root, textvariable=year)
e2.place(x=100, y=50)  # Using place to pack the label

cal = Button(text="Show Calendar", command=cal1)  # Creating Button
cal.place(x=130, y=90)  # Packing The button using place function

root.mainloop()



# Ques 3
# Calculator
from tkinter import *

def b0i():  # Creating a function to add 0 in String Variable
    global ent
    ent.set(ent.get()+'0')  # Adding 0 to the string
    inoutvar.update()


def b1i():  # Creating a function to add 1 in String Variable
    global ent
    ent.set(ent.get()+'1')  # Adding 1 to the string
    inoutvar.update()


def b2i():  # Creating a function to add 2 in String Variable
    global ent
    ent.set(ent.get()+'2')  # Adding 2 to the string
    inoutvar.update()


def b3i():  # Creating a function to add 3 in String Variable
    global ent
    ent.set(ent.get()+'3')  # Adding 3 to the string
    inoutvar.update()


def b4i():  # Creating a function to add 4 in String Variable
    global ent
    ent.set(ent.get()+'4')  # Adding 4 to the string
    inoutvar.update()


def b5i():  # Creating a function to add 5 in String Variable
    global ent
    ent.set(ent.get()+'5')  # Adding 5 to the string
    inoutvar.update()


def b6i():  # Creating a function to add 6 in String Variable
    global ent
    ent.set(ent.get()+'6')  # Adding 6 to the string
    inoutvar.update()


def b7i():  # Creating a function to add 7 in String Variable
    global ent
    ent.set(ent.get()+'7')  # Adding 7 to the string
    inoutvar.update()


def b8i():  # Creating a function to add 8 in String Variable
    global ent
    ent.set(ent.get()+'8')  # Adding 8 to the string
    inoutvar.update()


def b9i():  # Creating a function to add 9 in String Variable
    global ent
    ent.set(ent.get()+'9')  # Adding 9 to the string
    inoutvar.update()


def clear():  # Creating the clear function to clear the string
    global ent
    ent.set("")
    inoutvar.update()


def equal():
    global ent
    # Creating A Variable and using eval function to calculate the value
    variable = eval(inoutvar.get())
    ent.set(variable)  # Setting the String
    inoutvar.update()  # Update the screen


def plus():  # Creating a function to add plus in string
    global ent
    ent.set(ent.get() + '+')  # Setting the String
    inoutvar.update()


def sub():  # Creating a function to add subtract in string
    global ent
    ent.set(ent.get()+'-')  # Setting the String
    inoutvar.update()  # Update the screen


def mul():  # Creating a function to add multiply in string
    global ent
    ent.set(ent.get() + '*')  # Setting the String
    inoutvar.update()  # Update the screen


def div():  # Creating a function to add division in string
    global ent
    ent.set(ent.get() + '/')  # Setting the String
    inoutvar.update()  # Update the screen


root = Tk()
root.geometry("400x400")
label1 = Label(text="Calculator", font="comicsans 20 bold")
label1.pack(padx=20)
ent = StringVar()
inoutvar = Entry(textvariable=ent, font="comicsans 30 bold")
inoutvar.pack(padx=20)  # Packing the entry column and padding it

# Creating a button named 0 and given a command to add 0 in the string
button0 = Button(text="0", padx=20, command=b0i, font="comicsans 14 bold")
button0.place(x=160, y=220)  
# Creating a button named 1 and given a command to add 1 in the string
button1 = Button(text="1", padx=20, command=b1i, font="comicsans 14 bold")
button1.place(x=80, y=100) 
# Creating a button named 2 and given a command to add 2 in the string
button2 = Button(text="2", padx=20, command=b2i, font="comicsans 14 bold")
button2.place(x=160, y=100) 
# Creating a button named 3 and given a command to add 3 in the string
button3 = Button(text="3", padx=20, command=b3i, font="comicsans 14 bold")
button3.place(x=240, y=100)  
# Creating a button named 4 and given a command to add 4 in the string
button4 = Button(text="4", padx=20, command=b4i, font="comicsans 14 bold")
button4.place(x=80, y=140)  
# Creating a button named 5 and given a command to add 5 in the string
button5 = Button(text="5", padx=20, command=b5i, font="comicsans 14 bold")
button5.place(x=160, y=140)  
# Creating a button named 6 and given a command to add 6 in the string
button6 = Button(text="6", padx=20, command=b6i, font="comicsans 14 bold")
button6.place(x=240, y=140)  
# Creating a button named 7 and given a command to add 7 in the string
button7 = Button(text="7", padx=20, command=b7i, font="comicsans 14 bold")
button7.place(x=80, y=180)  
# Creating a button named 8 and given a command to add 8 in the string
button8 = Button(text="8", padx=20, command=b8i, font="comicsans 14 bold")
button8.place(x=160, y=180) 
# Creating a button named 9 and given a command to add 9 in the string
button9 = Button(text="9", padx=20, command=b9i, font="comicsans 14 bold")
button9.place(x=240, y=180) 
# Creating a button named + and given a command to add + in the string
buttonplus = Button(text="+", padx=20, command=plus, font="comicsans 14 bold")
buttonplus.place(x=80, y=260, width=67)  
# Creating a button named - and given a command to add - in the string
buttonsub = Button(text="-", padx=20, command=sub, font="comicsans 14 bold")
buttonsub.place(x=160, y=260, width=67)  
# Creating a button named X and given a command to add X in the string
buttonmul = Button(text="X", padx=20, command=mul, font="comicsans 14 bold")
buttonmul.place(x=240, y=260, width=67)  
# Creating a button named / and given a command to add / in the string
buttondiv = Button(text="/", padx=20, command=div, font="comicsans 14 bold")
buttondiv.place(x=80, y=300, width=67)  
# Creating a button named = and given a command to evaluate and update the string
buttonequal = Button(text="=", padx=20, command=equal,
                     font="comicsans 14 bold")
buttonequal.place(x=160, y=300, width=67)  # Placing it at (160,300)
# Creating a button named C and given a command to clear the string
buttonclear = Button(text="C", padx=20, command=clear,
                     font="comicsans 14 bold")
buttonclear.place(x=240, y=300, width=67)  # Placing it at (240,300)
root.mainloop()

# Ques 4
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
        
arr = [23, 12, 33, 34]
n = len(arr)
quickSort(arr, 0, n - 1)

print("Sorted array is: ", arr)


# Ques 5
n = int(input())
li = list(map(int, input().strip().split()))
# Part 1
li.sort()
print("Sorted array is:", li)

# Part 2
flag = False
low = 0
high = n
count = 0
ind = -1
to_find = int(input())
while(low < high):
    mid = low + (high - low) // 2
    if(int(li[mid]) == to_find):
        flag = True
        ind = mid
        print("Value is at index:", mid)
        break
    elif li[mid] > to_find:
        high = mid - 1
    else:
        low = mid + 1
if flag == False:
    print("Error")

# Part 3
if(ind == -1):
    print("No element\n")
else:
    i = mid
    j = mid
    count = 0
    for k in range(0, max(i, n - j)):
        if(i >= 0 and li[i] == to_find):
            count += 1
            i -= 1
        if(j < n and li[j] == to_find):
            count += 1
            j += 1
    print("Total number of occurances is:", count - 1)



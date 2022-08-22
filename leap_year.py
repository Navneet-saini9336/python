# Python Program to Check Leap Year

def leap(y):
    if y%100==0 and y%400==0:#must satisfy bot condition.
        print("Leap Year.")
    elif y%100!=0 and y%4==0:#must satisfy bot condition.
        print("Leap Year.")
    else:
        print("Not Leap Year.")

a = int(input("Enter year : "))
leap(a)

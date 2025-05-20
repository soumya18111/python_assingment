#................................calculator app.........................
#function creat
def addition(num1,num2):
    result = num1+num2
    print("{0}+{1}={2}".format(num1,num2,result))
def subtraction(num1,num2):
    result = num1-num2
    print("{0}-{1}={2}".format(num1,num2,result))

def multification(num1,num2):
    result = num1*num2
    print("{0}*{1}={2}".format(num1,num2,result))

def division(num1,num2):
    if num2==0:
        print("can't do divide by zero")
    else:
        result = num1/num2
        print("{0}/{1}={2}".format(num1,num2,result))
#display part
while True:
    print("What do you want to do")
    print("1 for addition")
    print("2 for subtraction")
    print("3 for multification")
    print("4 for division")
    print("Enter Q or q To exit the calculator")

#user input - 2digit number
    choice= input("Enter your choice: ")
    if choice == "q" or choice == "Q":
        break
#taking a 2 number as a input

    num1= float(input("enter number one: "))
    num2 = float(input("enter number two: "))

#condition part
    if choice=='1':
        addition(num1,num2)
    elif choice=='2':
        subtraction(num1,num2)
    elif choice== '3':
        multification(num1,num2)
    elif choice== '4':
        division(num1,num2)
    else:
        print("Invalid choice")
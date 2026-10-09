#Write a program to find the greatest of # number entered by the user
num1=int(input("Enter 1st number = "))
num2=int(input("Enter 2nd number = "))
num3=int(input("Enter 3rd number = "))
if ( num1>num2 and num1>num3):
    print("1st number is greatest")
elif( num3>num2 and num3>num1):
    print("3rd number is greatest")
else:
    print("2nd number is greatest")
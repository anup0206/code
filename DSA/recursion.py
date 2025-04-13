
def factorial(num):
    if (num ==1 or num==0):
        return 1
    else:
        return num * factorial(num -1)

num = int(input("Enter the number to fimd factorial : "))
print(f"The factorial of {num} is {factorial(num)}")

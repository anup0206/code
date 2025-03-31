

# def greatestNum(a,b,c):
#     if a > b and a > c:
#         print(f"The gratest number is {a}")
#     elif b> a and b > c:
#         print(f"The gratest number is {b}")
#     else:
#         print(f"The gratest number is {c}")

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# c = int(input("Enter third number : "))

# greatestNum(a,b,c)



# a = int(input("Enter temperature in celsius number : "))
# cal = a * (9/5) + 32
# print(f"The temperature in farenight is {cal}")


# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n - 1)

# a = int(input("Enter first number : "))
# print(sum(a))


    

# a = int(input("Enter  number : "))
# for i in range( a ,0 , -1):
#         for j in range( 0 , i-1):
#             print("*", end = " ")
#         print("\r")


# def convertin(num , unit):
#     if unit.lower()=="inch":
#         nume = num* 2.54
#         return f"The conversion of {num} inch is {nume} cm"
#     elif unit.lower()=="cm":
#         nume = num/2.54
#         return f"The conversion of {num} cm  is {num} cm"
#     else:
#         return f"PLEASE ENTER CORRECT UNIT......."
# num = float(input("Enter the number : "))

# unit= input("Enter inch to convert in cm or cm  in inch ")

# print(convertin(num ,unit))


# def remlist():
#     li= []
#     ine = int(input("How many elements u want to enter"))
#     for i in range (0 , ine):
#         user= input("Enter the elements in list ")
#         li.append(user)
#     rem=input("Enter the word want to remove from list : ")
#     li = [item for item in li if item.lower() != rem.lower()]
#     li = [item.strip() for item in li]
#     return li

# print(remlist())

# def multiply(num):
#     for i in range (0,11):
#         print(f"The multiplication table of {num} is {num} * {i} = {num * i} ")

# num = int(input("Enter the number to print multiply : "))
# print(multiply(num))
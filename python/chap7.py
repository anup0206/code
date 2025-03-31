# name_list = ["Anup","anupam","anisha","RIshi","Kalpana","Aarushi"]
# i =0 
# while i < len(name_list):
#     print(name_list[i])
#     i+=1[]

# n= int(input("Enter the number : "))

# i = 0 
# while i<11:
#     print(f"The multiplication table of {n} is {n} * {i} ={n*i}")
#     i = i+1


# for i  in range(1,11):
#     print(f"The multiplication table of {n} is {n} * {i} = {n*i}")


# l= ["Harry", "Soham", "Sachin", "Rahul"]
# for i in range(len(l)):
#     if l[i].startswith("S"):
#         print("Ohayo", l[i])


# def is_prime(n):
#     if n < 2:
#         return False  # 0 and 1 are not prime
#     for i in range(2, int(n**0.5) + 1):  # Check divisibility up to sqrt(n)
#         if n % i == 0:
#             return False  # If divisible, not prime
#     return True  # If no divisors found, it's prime

# # Taking user input
# num = int(input("Enter a number: "))

# # Checking and printing result
# if is_prime(num):
#     print(f"{num} is a Prime number.")
# else:
#     print(f"{num} is NOT a Prime number.")


# n= int(input("Enter the number : "))
# sum = 0
# i = 1
# while i<=n:
#     sum = sum+i
#     i=i+1
    
# print("The sum of number is",sum)


# def factorial(num):
#     if num == 0 or num==1:
#         return 1
#     else:
#         return num * factorial(num - 1)    

# num = int(input("Enter the number "))

# result=factorial(num)
# print("The factorial of " +str(num) +" is " +str(result) )




n= int(input("Enter the number : "))
for i  in range(10,0,-1):
    print(f"The multiplication table of {n} is {n} * {i} = {n*i}")


# file_names = ["1.txt", "2.txt", "3.txt"]

# for file in file_names:
#     try:
#         with open(file, "r") as f:
#             print(f"{file} opened successfully.")
#     except FileNotFoundError:
#         print(f"{file} is missing.")




# numbers = [1, 42, 33, 674, 57,6,87,88,9,11]
# for i , value in enumerate(numbers):
#     if i in [ 2 ,4, 6,]:
#         print(i +1, value)



# num = int(input("Enter the number for table : "))
# list1 = [f"{num} * {i} = {num*i} " for i in range (1,11)]
# print("\n".join(list1))



# num1 = int(input("Enter the number : "))
# num2= int(input("Enter the number : "))
# try:
#     calculate= num1 / num2 
#     if num2 != 0:
#         print(f"The division of two number is {calculate}")
# except ZeroDivisionError as e:
#     print("Error  : ",e)



num = int(input("Enter the number for table : "))
list1 = [f"{num} * {i} = {num*i}" for i in range(1, 11)]

with open("table.txt", "w") as f:
    # Write each multiplication result on a new line
    f.write("\n".join(list1))

# Optionally, print it to the console as well
print("\n".join(list1))

# a = int(input("Enter your age : "))
# if(a>= 18):
#     print("Yes")
# else:
#     print("no")





# wap to check greatest
# num1 = int(input("Enter first number "))
# num2 = int(input("Enter second  number "))
# num3 = int(input("Enter third number "))
# num4 = int(input("Enter fourth number "))
# if(num1>num2 and num1>num3 and num1>num4):
#     print("The greatest number is ", num1)
# elif(num2>num1 and num2>num3 and num2>num4):
#     print("The greatest number is ", num2)
# elif(num3>num1 and num3>num2 and num3>num4):
#     print("The greatest number is ", num3)
# else:
#     print("The greatest number is ", num4)




# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# def check_pass_fail(marks):
#     total_marks = sum(marks)
#     total_percentage = (total_marks / 300) * 100 

#     if total_percentage >= 40 and all(mark >= 33 for mark in marks):
#         return f"Congratulations! You passed with {total_percentage:.2f}%."
#     else:
#         return f"Sorry, you failed with {total_percentage:.2f}%."

# marks = []
# for i in range(1, 4):
#     mark = float(input(f"Enter the marks in Subject {i} (out of 100): "))  
#     marks.append(mark)  


# result = check_pass_fail(marks)
# print(result)



# scam_key = ["Make a lot of money","buy now","subscribe this","click this"]

# wrd = "vvv fASFFFFA buy now adakdjakjd"
# if any(keyword.lower() in wrd.lower() for keyword in scam_key):
#     print("Scam comment detected !!!!!!!")
# else:
#     print("Not a Scam comment ")


# char = input("Enter your name : ")

# if(len(char)>10):
#     print("Character have length more than 10 ")
# else:
#     print("Character havenot length more than 10 ")


# name_list = ["Anup","anupam","anisha","RIshi","Kalpana","Aarushi"]

# search_name =  input("Enter your name : ")

# if any(word.lower() in search_name.lower() for word in name_list):
#     print("Name is present in list")
# else:
#     print("Name is not present in list")



# subject1 = int(input("Enter first subject number "))
# subject2 = int(input("Enter secon subject  number "))
# subject3 = int(input("Enter third subject number "))
# subject4 = int(input("Enter fourth subject  number "))
# subject5 = int(input("Enter fifth subject  number "))
# total_marks = (subject1+subject2+subject3+subject4+subject5)
# grade = (total_marks/500)*100
# print(f"The total marks you obtained is {total_marks}")

# if(grade >= 90):
#     print("EXCELLENT GARDE")
# elif(grade>80 and grade<90):
#     print("A GRADE")
# elif(grade>70 and grade<80):
#     print("B GRADE")
# elif(grade>60 and grade<70):
#     print("C GRADE")
# elif(grade>50 and grade<60):
#     print("D GRADE")
# elif(grade <50):
#     print("F GRADE")

post = input("Enter the post: ")  


if "harry" in post.lower():
    print("The post is talking about Harry!")
else:
    print("The post is NOT talking about Harry.")

# wap to display name

# a = input("Enter name: ").capitalize()
# print("Good Afternoon " + a)

# wap to fill letter templste
# from datetime import datetime

# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# Name = input("enter name ").capitalize()
# Date = datetime.today().strftime('%Y-%m-%d')
# # print(f'''
# # Dear {Name},
# # You are selected!
# # {Date}
# # ''')
# letter = letter.replace("<|Name|>", Name).replace("<|Date|>",Date)
# print(letter)

# wap to detectdouble string

Name = input("Enter name: ")

if "  " in Name:
    print("Double space detected!")
else:
    print("No double spaces found.")




# replace double space to single 
Name = input("enter name ")
if Name.find("  ") != -1:
   Name =  Name.replace("  ", " ")
   print(Name)
else:
    print("no duble space")


letter = "Dear Harry,\n\tThis Python course is nice.\nThanks!"
print(letter)

# import re

# search = "twinkle"

# # Open the file in read mode
# with open("poem.txt", "r", encoding="utf-8") as f:
#     text = f.read()

# # Correct way to use the variable inside regex
# if re.search(rf"\b{search}\b", text, re.IGNORECASE):
#     print("The word is found")
# else:
#     print("Word not found")






# import random

# def guessNum():
#     numTOguess= random.randint(1,100)
#     attempt=0
#     max_score = 100
#     score =max_score


#     print(" Welcome to the Number Guessing Game!")
#     print("I have chosen a number between 1 and 100. Try to guess it.")
#     print("Your score decreases with each wrong guess. Try to k eep it high!")  

#     while True:
#         try:
#             guess=(int(input("Enter the number u guess  : ")))
#             attempt +=1
#             score-=5
#             if guess > numTOguess:
#                 print("TOO HIGH BABY.. \n TRY AGAIN\n")
#             elif guess < numTOguess:
#                 print("TOO LOW BABY.. \n TRY AGAIN\n")
#             else:
#                 print(f"Congratulations! You have guessed in {attempt} attempts ")
#                 print(f"Your final score is {max(score, 0)}")
#                 break
#         except ValueError:
#                 print("Please input valid num")
#     return score

# player_score=guessNum()

# try:
#     try:

#         with open("hi-score.txt", "r") as f:
#             content= f.read().strip()
#             if content and content.startswith("The high score is "):
#                 prev_high_score= int(content.spit()[-1])
#             else:
#                 prev_high_score=0
#     except FileNotFoundError:
#         prev_high_score=0

#     if player_score > prev_high_score:
#             with open("hi-score.txt", "w") as f:
#                 f.write(f"The high score is {player_score}")
#             print(f"New high score: {player_score}!")

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     print("Game execution completed.")



 


# for i in range(2, 21):  
#     with open(f'file_{i}.txt', 'w') as f:  
#         f.write(f"Multiplication Table of {i}\n")  
#         f.write("=" * 25 + "\n") 
#         for j in range(1, 11):  
#             result = i * j  
#             f.write(f"{i} * {j} = {result}\n")  
#         f.write("\n")    






# import re
# List of words to censor
# search = ["donkey", "yo"]

# def censor_text(text, search):
#     for word in search:
#         text = re.sub(rf"\b{word}\b", "*" * len(word), text, flags=re.IGNORECASE)
#     return text

# # Read the file
# with open("donkey.txt", "r") as f:
#     text = f.read().strip()

# # Check if file is empty
# if not text:
#     print("File is empty")
# else:
#     print("File is not empty")

#     # Check if any word in 'search' appears in the text
#     if any(re.search(rf"\b{word}\b", text, re.IGNORECASE) for word in search):
#         censored_text = censor_text(text, search)

#         # Write the censored text back to the file
#         with open("donkey.txt", "w") as f:
#             f.write(censored_text)

# print("Censorship complete!")




# import re
# word = "Python"

# with open("sample.log", "r" ,encoding="utf-8") as f:
#     text = f.read().strip()

# if re.search(rf"\b{word}\b" , text, re.IGNORECASE):
#     print("Found word")
# else:
#     print("Not found")



# import re
# worde = "Python"
# i = 0

# with open("sample.log", "r" ,encoding="utf-8") as f:
#     for line in f:
#         i = i+1
#         if re.search(rf"\b{worde}\b" , line, re.IGNORECASE):
#             print(f"Found word in {i} line in file")




# with open("sample.log", "r" ,encoding="utf-8") as f,open("copy.log", "w" ,encoding="utf-8") as g:
#     for lines in f:
#         g.write(lines)

# org = open("sample.log", "r" ,encoding="utf-8")
# des = open("copy.log", "w" ,encoding="utf-8") 
# line = org.readline()

# while line:
#     des.write(line)
#     line = org.readline()
# org.close()
# des.close()





# import filecmp
# org = "sample.log"
# des = "copy.log"

# if filecmp.cmp(org,des, shallow = False):
#     print("file are identical")
# else :
#     print("file are different")

# def compare_files(file1, file2):
#     with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
#         line_num = 1
#         for line1, line2 in zip(f1, f2):
#             if line1 != line2:  # Check if lines are different
#                 print(f"Files are different at line {line_num}")
#                 print(f"Line in {file1}: {line1}")
#                 print(f"Line in {file2}: {line2}")
#                 return False
#             line_num += 1
        
#         # If one file is longer than the other
#         if f1.readline() or f2.readline():
#             print("Files have different lengths")
#             return False
        
#         print("Files are identical")
#         return True

# file1 = "sample.log"
# file2 = "copy.log"
# compare_files(file1, file2)


# import os

# file_path = "copy.log"

# if os.path.exists(file_path):
#     try:
#         os.remove(file_path)
#         print("File deleted successfully.")
#     except PermissionError:
#         print("Permission denied: Unable to delete the file.")
#     except OSError as e:
#         print(f"Error deleting file: {e}")
# else:
#     print("File not found.")



# import shutil

# file_path = "copy.log"
# backup_path = file_path + ".bak"

# try:
#     shutil.copy(file_path, backup_path)  # Create a backup
#     open(file_path, "w").close()  # Wipe the content
#     print(f"Content of '{file_path}' has been wiped out. Backup saved as '{backup_path}'.")
# except Exception as e:
#     print(f"Error: {e}")
    
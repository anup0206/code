
# import random

# def guess():
#     random_number = int(random.randint(1,100))
#     attempts= 0
#     max_score =100
#     score =max_score
#     print(" Welcome to the Number Guessing Game!")
#     print("I have chosen a number between 1 and 100. Try to guess it.")
#     print("Your score decreases with each wrong guess. Try to keep it high!")  

#     while True:
#         try:
#             n = int(input("Enter the number you guess : "))
#             attempts += 1
#             score -=5

#             if (n > random_number):
#                 print("SORRY BABY .../n TOO HIGH/n")
#             elif (n < random_number):
#                 print("SORRY BABY .../nTOO LOW")
#             else:
#                 print(f"You have guessed same as random {n} in {attempts} guesses")
#                 print(f"Your final score is {max(score, 0)}")
#                 break
#         except ValueError:
#                 print(f"Please input the valid number")
#     return score
# game =guess()

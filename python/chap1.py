# print("Twinkle twinkle little star.\nHow I wonder what you are.\\nUp above the world so high. \nLike a diamond in the sky. \nTwinkle twinkle little star. \nHow I wonder what you are.")

# n = 5
# for i in range(1, 11):
#     m = n * i
#     print(f"The table of 5 is {n} * {i} = {m}")


import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
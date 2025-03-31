# Write a program to create a dictionary of Hindi words with values as their English
# translation.


# hindi_to_english = {
#     "नमस्ते": "hello",
#     "प्यार": "love",
#     "दोस्त": "friend",
#     "खुशी": "happiness",
#     "शांति": "peace"
# }

# while True:zz
#     print("\nHindi to English Dictionary")
#     word = input("Enter a Hindi word to look up (or type 'exit' to quit): ")
    
#     if word.lower() == "exit":
#         print("Goodbye!")
#         break
    
#     translation = hindi_to_english.get(word)
    
#     if translation:
#         print(f"The English translation of '{word}' is: {translation}")
#     else:
#         print("Word not found in dictionary.")


# a program to input eight numbers from the user and display all the unique
# numbers (once).

# s = set()
# for i in range (8):
#     a= int(input(f"Enter the number { i+1} "))
#     s.add(a)

# for i in s:
#     print(i)


# s= (18,"18" )
# print(s)


# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(len(s))

# create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are uniqu

# fav_languages = {}
# for i in range(4):
#     name = input("ENTER YOUR NAME ")
#     lang = input("Enter your fav language ")
#     fav_languages[name] = lang

# print("\nFavorite Languages Dictionary:")
# print(fav_languages)

d= {}
d.update({"anup":100})
print(d)

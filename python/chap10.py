# class Programmer:
#     def __init__(self,name,age,gender,language ,company):
#         self.name= name
#         self.age= age
#         self.gender=gender
#         self.language= language
#         self.company= "Microsoft"
    
#     def display_info(self):
#         print(f"Name : {self.name}    Age :{self.age}   Gender : {self.gender}      Language :{self.language}     Company : {self.company} ")

# p1 = Programmer("Anupam",20,"Male","Python","Microsoft")
# p2 = Programmer("Anupa",20,"Female","Python","Microsoft")
# p1.display_info()
# p2.display_info()




# import math
# class Calculator:
#     def __init__(self,number):
#         self.number = number
       

#     def square(self):
#         print(f"The square of {self.number} is {pow(self.number, 2)}")
      
#     def cube(self):
#         print(f"The cube of {self.number} is {pow(self.number, 3)}")
#     def sqrt_root(self):
#         print(f"The square root of {self.number} is {math.sqrt(self.number)}")

# calculator = Calculator(9)

# # Calling methods
# calculator.square()
# calculator.cube()
# calculator.sqrt_root()




# import math
# class Calculator:
#     def __init__(self,number):
#         self.number = number
       

#     def square(self):
#         print(f"The square of {self.number} is {pow(self.number, 2)}")
      
#     def cube(self):
#         print(f"The cube of {self.number} is {pow(self.number, 3)}")
#     def sqrt_root(self):
#         print(f"The square root of {self.number} is {math.sqrt(self.number)}")
#         @staticmethod
#     def greet():
#         name =input("Enter your name please : ")
#         print(f"Hello {name}")
# Calculator.greet()
# calculator = Calculator(9)

# # Calling methods
# calculator.square()
# calculator.cube()
# calculator.sqrt_root()




# class Train:
#     def __init__(self, name="", full_size=0, ticket_booked=0, fare=0):
#         self.name = name
#         self.full_size = full_size
#         self.ticket_booked = ticket_booked
#         self.fare = fare

#     def user_input(self):
#         self.name = input("Enter the name of the train: ")
#         self.full_size = int(input("Enter the total number of seats in the train: "))
#         self.ticket_booked = int(input("Enter the number of seats already booked: "))
#         self.fare = int(input("Enter the price of one ticket: "))

#     def ticket_book(self):
#         ticket_booking = int(input("Enter the number of tickets you want to book: "))
        
#         # Check if enough seats are available
#         if self.ticket_booked + ticket_booking <= self.full_size:
#             self.ticket_booked += ticket_booking  # Update booked seats
#             print(f"{ticket_booking} ticket(s) booked successfully!")
#         else:
#             print("Sorry, not enough seats available.")

#     def get_status(self):
#         print(f"Train Name: {self.name}")
#         print(f"Total Seats: {self.full_size}")
#         print(f"Available Seats: {self.full_size - self.ticket_booked}")

#     def get_fare_info(self):
#         print(f"The fare for this train is ₹{self.fare} per ticket.")


# # Creating an object of the Train class
# obj = Train()
# obj.user_input()  # Get details from user
# obj.get_fare_info()  # Show fare info
# obj.get_status()  # Show available seats
# obj.ticket_book()  # Book tickets
# obj.get_status()  # Show updated available seats




            
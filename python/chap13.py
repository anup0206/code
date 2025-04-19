
# installing virtual environment and copying its package into another virtual envirom=nment 

# Create the first virtual environment:
# python3 -m venv env1

# Activate the virtual environment (for Linux):
# source env1/bin/activate

# Install some packages (e.g., requests and numpy):
# pip install requests numpy

# Generate a requirements.txt file: 
#  create a requirements.txt file that contains the list of all installed packages in env1:
# pip freeze > requirements.txt


# Create the Second Virtual Environment
# python3 -m venv env2

# Activate the  second virtual environment (for Linux):
# source env2/bin/activate

# Install packages from the requirements.txt file: In your second environment, run:

# pip install -r requirements.txt

# Result:

# The second virtual environment (env2) will now have the same packages installed as the first one (env1).




# name = input("Enter your name : ")
# mark = input("Enter your mark : ")
# phone = input("Enter your phone : ")

# template = f"The name of the student is {name}, his marks are {mark} and phone number is {phone}"
# print(template.format(name,mark,phone))




# table= lambda n,i: n*i
# result = [str(table(7,i)) for i in range (1,11)] 
# print("\n".join(result))



# # List of numbers
# nums = [5, 6, 7, 9, 0, 90, 55, 60, 15, 54, 69]

# # print("Numbers divisible by 5 using for loop:")
# # for num in nums:
# #     if num % 5 == 0:
# #         print(num)

# # Using filter() and lambda to filter numbers divisible by 5
# div_by_5 = list(filter(lambda x: x % 5 == 0, nums))
# print("\nNumbers divisible by 5 using filter and lambda:")
# print(div_by_5)



# from functools import reduce
# nums = [5, 6, 7, 9, 0, 90, 55, 60, 15, 54, 69]
# max = reduce(lambda x, y: x if x > y else y , nums )
# print(max)


# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
# app.run()

# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/')
# def form():
#     return '''
#         <form method="POST" action="/greet">
#             <label>Your name: <input type="text" name="username"></label>
#             <input type="submit">
#         </form>
#     '''

# @app.route('/greet', methods=['POST'])
# def greet():
#     name = request.form['username']
#     return f"Hello, {name}!"
    
# app.run(debug=True)

from flask import Flask, render_template_string, request

app = Flask(__name__)

# Predefined user credentials
valid_username = "user"
valid_password = "password123"

# Login page
@app.route('/')
def login_form():
    return render_template_string('''
        <form method="POST" action="/login">
            <label>Username: <input type="text" name="username"></label><br>
            <label>Password: <input type="password" name="password"></label><br>
            <input type="submit" value="Login">
        </form>
    ''')

# Handle login POST request
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Check if the credentials match
    if username == valid_username and password == valid_password:
        return f"Welcome, {username}!"
    else:
        return "Invalid username or password. Please try again."

app.run(debug=True)


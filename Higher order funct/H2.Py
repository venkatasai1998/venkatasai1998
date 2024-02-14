# def d1(para1,para2,para3):

#     return "para1",para1,para2,para3

# def d2():

#     return "para2"

# def d3():

#     return "para3"

# def d4():

#     return "para4"


# d = d1(d2(),d3(),d4())
# print(d)

def d1(func):
    def wrapper(password):
        # Check if the password is correct
        if password == "secretpassword":
            # If the password is correct, execute the original function
            return func()
        else:
            # If the password is incorrect, return an error message
            return "Incorrect password! Access denied."
    return wrapper

@d1
def d3():
    return "Access granted. Welcome to the system."

# Asking for password input
password_input = input("Enter the password: ")

# Call the decorated function with the password
result_d3 = d3(password_input)

# Print the result
print(result_d3)


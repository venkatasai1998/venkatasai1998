#global variable :we can access the variable inside or ouside the function 
#local variable : we can access the variable insode the function only

# y = 20  # This is a global variable

# def my_function():
#     z=30
#     print("Inside function:", z)
    

#     print("Inside function:", y)  # Accessing global variable


# my_function()
# # print("outside function:", y)


# #globals()
# global_var = "I am a global variable"
# def my_function():

#     globals()['global_var']="local_var"
    
#     print("inside the function:", global_var)


# my_function()



# #locals() method
# def my_function():
#     local_var = "I am a local variable"
#     local_var = "I am a glob                   al variable"
    
#     local_symbol_table = locals()["local_var"]
#     print("Local variable inside the function:", local_symbol_table)
#     print("Local variable inside the function:", local_symbol_table)

# my_function()


# global keyword : using global method we can bring local variable into global and access it globally


name= "sai"

def Names():
    global C_names

    C_names=["kumar","vinay","kiran"]

    print("global_var:", name)


Names()
print(C_names)






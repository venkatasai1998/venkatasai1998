#file is simply a container that store data permanently.Here file is input in your program. file is simply a sequence of bytes that stores data permanently in the Drives.

# there are 3 keywords to handle errors
#1) Try : bussiness logic
#2) Expect : handling errors
#3) finally : closing connections

# try:
#   L1=[10,20]
#   L1[2]=[30]   #IndexError: list assignment index out of range

# except IndexError as e:
#   print("Expection",e)   #Expection list assignment index out of range

#   print("index out of range")



# create file and insert data
# if you want to perform read and write operarions initailly you need to open the file 
#syntax : open("filename","mode")

#task 1
  
# f=None    #global variable anywhere you can call if you are not used then finally block should be undefined

# try:
#   f=open("one.txt","w")
#   s=input("enter your name: ")
#   f.write(s)
# except FileNotFoundError as e:
#   print("exception",e)

# finally:
#   f.close()
  
#task 2 Read the data from the file using read method          

# try:
#   f=open("one.txt","r")
#   print(f.read())

# except FileNotFoundError as e:
#   print("exception",e)

# finally:
#   f.close()

# task 3 : read the data from file using loop
# try:
#   f=open("one.txt","r")
#   for i in f:
#     print(i)
  
# except FileNotFoundError as e:
#   print("exception",e)

# finally:
#   f.close()

#task 4: write and read data using writelines

# f=None    

# try:
#   f=open("two.txt","w")
#   L1=["Nameone","Nametwo","Namethree","Namefour"]
#   f.writelines(L1)                      #writelines() method is used to write a sequence of strings to a file

#   f=open("two.txt","r")
#   print(f.read())   #NameoneNametwoNamethreeNamefour
 
# except FileNotFoundError as e:
#   print("exception",e)

# finally:
#   f.close()


#task 5 : write and read data using write() and tell() method
# tell method tells the position of the crusor
# nested try and except
try :
  f=None    
  try:
    f=open("three.txt","w") 
    s=input("Enter your name")
    f.write(s)

  except FileNotFoundError as e:
    print("exception",e)

  try:
      
      f=open("three.txt","r")
      print(f.read(2))      #sa
      print(f.tell())       #2
      print(f.read())
      print(f.tell())       #9

  except FileNotFoundError as e:
      print("exception",e)
finally:
  f.close()
  

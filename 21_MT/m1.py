

#Thread is a class

# import threading

# t1=threading.current_thread()
# print(t1.name)

# t2=threading.main_thread()
# print(t2.name)

# if threading.current_thread()==threading.main_thread():
#     print("Main thread as same")

# else:
#     print("other thread")



#get the thread name and change the thread name
import threading
#reference=modulename.objectname()
# t1=threading.Thread()
# print(t1.name)

# t1.name="Hello"
# print(t1.name)


# t2 = threading.Thread(name='CustomThreadName')  #assigning custom name to the thread
# print(t2.name)    


# ident method

# t1=threading.current_thread()
# t2=threading.main_thread()

# if t1==t2:

#     print("True")
#     print(t1.ident)
#     print(t2.ident)


# else:

#     print("false")


#task: to call function in threading we use target as a property
    
from threading import Thread

def displaydata():

    i=0

    while i <= 10:

        print(i)

        i+=1

Thread(target=displaydata())

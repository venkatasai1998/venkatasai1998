# selection statements(if,elif,else)

#if condition:                   condition either true or false
     #bussiness logic


#Task:
#Given an integer n , perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of 2  to  5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird

n=int(input('enter an integer:'))

if n%2==1:
    print("weird")

elif n in range(2,5):
    print("not weird")

elif n in range(6,20):
    print("weird")

elif n%2==0 and n>20:
    print("not weird")

else:
    print("condition failed")    
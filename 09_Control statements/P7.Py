a=[10,20,30,40]

while len(a)>4: 
      print(a.pop())

else:
      print("condition failed")



def calculate_sum(n):
    
    total = 0
    

    for i in range(n+1):  # range(0,101)
        total += i
    
    return total
    
result = calculate_sum(100)
print(result)



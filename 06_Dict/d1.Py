# dic{}

d1={}
print(d1,type(d1))   #{} <class 'dict'>


L1=[10,20,30,40,50]
print(L1[0])   #10
print(L1[4])   #50 

d2={}
d2[0]=10
d2[1]=20
d2['sai'] = 'kumar'
print(d2)    #{0: 10, 1: 20, 'sai': 'kumar'}


d3={0: 10, 1: 20, 'sai': 'kumar'}
print(d3[0],d3[1],d3['sai'])    #10 20 kumar

# Assigning a position to a list and dict
#L2=[10,20,30,40,50]
#print(L2[5])    #IndexError: list index out of range

d4={'a':10,'b':20,'c':30,'d':40,'e':50}
d4['f']=60
print(d4)  #{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}








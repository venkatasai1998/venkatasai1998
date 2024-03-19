import pandas as panda

#get the index position and element using series() method

# L1=[10,20,30,40,50]
# print(panda.Series(L1))

#customizing index position using series method
# L2=[10,20,30,40,50]
# print(panda.Series(L2,index=['a','b','c','d','e']))


# using Dataframe we get tabular data

d1={
    'Names':['Saikumar','yash','satish','Rajesh'],
    'city':['Hyd','nellore','tpty','chennai']
}

print(panda.DataFrame(d1))
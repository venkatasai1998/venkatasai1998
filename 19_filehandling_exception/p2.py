#seek method: seek method is used to change the position of the crusor

# f=None

# try:

#     f=open("three.txt","r")
#     print(f.tell())
#     print(f.read(2))
#     print(f.seek(0))
#     print(f.read())

# except FileNotFoundError as e:

#     print("exception",e)

# finally:

#     f.close()

# task : store normal data to binary format
#pickle method : used to convert data to binary as well as binary to normal data
#dump(iteration,fileobject)
# import pickle
# L1=["Nameone","Nametwo","Namethree","Namefour","Namefive"]
# f=open("four.dat","wb")
# pickle.dump(L1,f)   
# print("data stored")
# f.close()                   



#task :read normal data from binary data

# import pickle

# f=open("four.dat","rb")
# p=pickle.load(f)
# print(p)

# f.close()



# task : store the data into excel file

from openpyxl import Workbook

data =[
    ["Name","Age","city"],["sai","24","Nellore"],["yash","22","Hyd"],["yash","22","Hyd"]
]

wb=Workbook()
ws=wb.active

for row in data:

    ws.append(row)

file_open="one.xlsx"
wb.save(file_open)
print("data stored")

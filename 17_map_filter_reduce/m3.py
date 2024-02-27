employees=[
    {"firstName":"sai","Lastname":"Kiran","age":28},
    {"firstName":"sai","Lastname":"Ram","age":29},
    {"firstName":"sai","Lastname":"Krishna","age":26},
    {"firstName":"sai","Lastname":"Kumar","age":28},
    {"firstName":"sai","Lastname":"Nath","age":30},
]




# print(employees[0]["firstName"] ,"",employees[0]["Lastname"],"", employees[0]["age"])
# print(employees[1]["firstName"] ,"",employees[1]["Lastname"],"", employees[1]["age"])
# print(employees[2]["firstName"] ,"",employees[2]["Lastname"],"", employees[2]["age"])
# print(employees[3]["firstName"] ,"",employees[3]["Lastname"],"", employees[3]["age"])
# print(employees[4]["firstName"] ,"",employees[4]["Lastname"],"", employees[4]["age"])


# a=map(lambda x : x["firstName"]+" " +x["Lastname"],employees)
# print(list(a))


a=filter(lambda x:x["age"]>28,employees)
print(list(a))


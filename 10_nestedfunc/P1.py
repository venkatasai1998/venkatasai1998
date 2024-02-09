# for i in range(3):
#     for j in range(2):
#         print(f"({i}, {j})",end=" ")


i = 1
while i <= 3:
    print(f"Outer loop iteration: {i}")
    j = 1
    while j <= 2:
        print(f"Inner loop iteration: {j}")
        j += 1
    i += 1
list1 = [9, -15, 0, 57, -515, 999, 123, 98]
list2 = []
for i in list1:
    if i > 0:
        list2.append(1)
    elif i < 0:
        list2.append(-1)
    else:
        list2.append(0)

print(list1)
print(list2)
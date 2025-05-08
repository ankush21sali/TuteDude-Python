list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list : ",list1)

list2 = list1[:5]
print("Extract first five element : ",list2)

list3 = []
for item in list2:
    list3.insert(0, item)
print("Reversed extract element : ", list3)

list1 = [8,19,148,4]
list2 = [9,1,33,83]
list3 = []

for num1 in list1:
    for num2 in list2:
        print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
        list3.append(num1 * num2)

print(list3)

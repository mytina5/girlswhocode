#list = [ 5, 3, 7, 1, 8, 5]

#max = max(list)
#print(max)
list = [ 5, 3, 7, 1, 8, 5]
product = 1
for num in list:
    product *= num
print(product)

list2 = [2, 4, 6, 9]
list.append(list2)
print(list)

list.sort()
print (list)

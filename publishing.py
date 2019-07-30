import publishers
list_of_book = publishers.get_books()#test = True)

#print(list_of_book)

#print(list_of_book[0])
for row in list_of_book:
    print(sum(int(row["daily average"]["author revenue"])))

#total1 = sum([daily average][author revenue])
#print(total1)
#author = [daily average][author revenue]
#length = len(int(daily average, author revenue))
#print(length)

#for i in range

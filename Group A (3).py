# Write a Python program for department library which has N books, write functions for
# following:
# a) Delete the duplicate entries
# b) Display books in ascending order based on cost of books
# c) Count number of books with cost more than 500.
# d) Copy books in a new list which has cost less than 500.
# 4 Write a Python program that computes the net amount of a bank

def create (n, list):
    sublist = []
    for i in range (n):
        name = input("Enter Book name :") 
        cost = int(input("Enter Book cost : ")) 
        sublist.append(name)
        sublist.append(cost)
        list.append(sublist)
        sublist = []
    
def del_dup(list):
    for i in range (len(list)):
        for j in range (i, len(list) - i):
            if (list[i][1] == list[j][1]):
                list[j:j+1]
    
    
record = []
print ("*WELCOME TO LIBRARY*")

# records = int(input("Enter the number of records you want to add : "))
# create(records, record)
# del_dup(record)

record = [['okey', 12], ['okey', 123], ['adksjh', 123], ['okey', 123], ['adksjh', 13]]

list = record
for i in range (len(list)):
    for j in range (i+1 , len(list)):
        if (list[i][0] == list[j][0]):
            list.pop(i)
            padd 
        print (list)
# print (record)













# check

book = []

n = 100



for i in range (n):
    temp = []
    item = input("Name : ")
    if (item == "exit" or item == "Exit"):
        break
    cost = int(input("cost : "))
    temp.append(item)
    temp.append(cost)
    book.append(temp)


# to delete duplicate entries :)

# for i in range (len(book)):
#     for j in range (len(book) - i-1):
#         if (book[i][0] == book[i + j][0]):
#             # print("i = ", i, "j = ", j+i, "\n")
#             # print ("book i = ",book[i], "book j+i = ", book[j+i]) 
#             count = i+j
#         if (count > 0):
#             del book[count:count+1]
#         i = 0
            

# display books in ascending order of cost

for i in range (0, )


print (book)

# Write a Python program for department library which has N books, write functions for following:
# a) Delete the duplicate entries
# b) Display books in ascending order based on cost of books
# c) Count number of books with cost more than 500.
# d) Copy books in a new list which has cost less than 500.
# 4 Write a Python program that computes the net amount of a bank


def swap(list, a, b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp

def InPut (lib, n):
    print("Lets Enter Recordds :)")
    for i in range (n):
        item = []
        book = input("Enter book : ")
        if (book == "Exit" or book == "exit"):
            break
        cost = int(input("Enter cost : "))
        item.append(book)
        item.append(cost)
        lib.append(item)

def del_dup (lib):
    temp_lib = []
    [temp_lib.append(x) for x in lib if x not in temp_lib]
    return temp_lib

def sortoncost(lib):
    count = 0
    sortedlib = lib
    i = 0
    # print(sortedlib)
    for i in range (len(lib) - 1):
        if (lib[i][1] > lib[i+1][1]):
            swap(lib, i, i+1)
            count += 1
    if (count == 0):
        return sortedlib
    else :
        sortoncost(sortedlib)
    return sortedlib

def morethan500(lib):
    count = 0 
    for book in lib:
        if (book[1] > 500):
            count += 1
    return count

def bookmorethan500(lib):
    templib = []
    for i in range(len(lib)):
        if (lib[i][1] > 500):
            templib.append(lib[i])
    return templib

Library = []

num_of_books = int(input("enter total number of books in Library : ")) 
InPut(Library, num_of_books)

print("choose one :)")


print("Delete Duplicate :)")
print("original Library = ",Library)
print("del dup = ",del_dup(Library))

print("books with cost more than 500")
print(morethan500(Library))

print("og library = ", Library)
sortoncost(Library)
print("sorted Library = ",sortoncost(Library))

books_cost_more_than_500 = bookmorethan500(Library)
print(books_cost_more_than_500)
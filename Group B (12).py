# a) Write a Python program to store names and mobile numbers of your friends
#   in sorted order on names. Search your friend from list using binary search
#   (recursive and non- recursive). Insert friend if not present in phonebook

def fibonacci_search(lst, target):
    size = len(lst)
     
    start = -1
     
    f0 = 0
    f1 = 1
    f2 = 1
    while(f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
     
    while(f2 > 1):
        index = min(start + f0, size - 1)
        if lst[index][1] < target:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif lst[index][1] > target:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (lst[size - 1] == target):
        return size - 1
    return None

def conditioncheck(str1, str2):
    alph = "abcdefghijklmnopqurstuvwxyz"
    if alph.index(str1[0]) > alph.index(str2[0]):
        return 1
    elif alph.index(str1[0]) < alph.index(str2[0]):
        return 0
    else:
        return -1

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        print(mid)
        if conditioncheck(arr[mid][0], x) == -1:
            return mid
        elif conditioncheck(arr[mid][0], x) == 1:
            binarySearch(arr, l, mid-1, x)
        else:
            binarySearch(arr, mid+1, r, x)

rec = []
temp = []

# input from user
print("Name : done ---> to Exit")
while (1):
    temp = []
    name = input("Name : ")
    if name == "done" or name == "Done" : break
    num = int(input("Mobile Number : "))
    temp.append(name)
    temp.append(num)
    rec.append(temp)

sorted_rec = sorted(rec)
x = input("find name (using Binary Search) : ")
y = int(input("find Num (using Fibonacci Search) : "))


result = binarySearch(sorted_rec, 0, len(sorted_rec)-1, x)

print("Searching using Binary Search")
# print Result
if (result != None):
    print ("Found at index ", result)
    print(sorted_rec[result])
else: 
    print ("Friend not found")
    temp.append(x)
    temp.append(y)
    rec.append(temp)
    sorted_rec = sorted(rec)
    print(sorted_rec)

    
# b) Write a Python program to store names and mobile numbers of your friends in
#   sorted order on names. Search your friend from list using Fibonacci search. Insert
#   friend if not present in phonebook.



print("Searching Using Fibonacci Search")
if (fibonacci_search(sorted_rec, y) != None):
    print("Found At Index", fibonacci_search(sorted_rec, y))
    print(sorted_rec)
else :
    print("Not found")

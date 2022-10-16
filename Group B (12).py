# a) Write a Python program to store names and mobile numbers of your friends
#   in sorted order on names. Search your friend from list using binary search
#   (recursive and non- recursive). Insert friend if not present in phonebook

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
x = input("find name : ")


# Function call
result = binarySearch(sorted_rec, 0, len(sorted_rec)-1, x)

if (result != None):
    print ("Found at index ", result)
    print(sorted_rec[result])
else: 
    print ("Friend not found")
    num = int(input("Number : "))
    temp.append(x)
    temp.append(num)
    rec.append(temp)
    sorted_rec = sorted(rec)
    print(sorted_rec)

    
# b) Write a Python program to store names and mobile numbers of your friends in
#   sorted order on names. Search your friend from list using Fibonacci search. Insert
#   friend if not present in phonebook.


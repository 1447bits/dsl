# Write a Python program to store marks scored in subject “Fundamental of Data Structure” by
# N students in the class. Write functions to compute following:


def average(arr):
    avg = 0
    for i in range (len(arr)):
        avg += arr[i]
    return avg/len(arr)
    
def lowest(arr):
    low = arr[1]
    for i in arr:
        if i < low:
            low = i
        else :
            pass
    return low

def highest(arr):
    high = arr[1]
    for i in arr:
        if i > high:
            high  = i
        else :
            pass
    return high

def mostFrequent(arr):
    n = len(arr)
    maxcount = 0
    element_having_max_freq = 0
    for i in range(0, n):
        count = 0
        for j in range(0, n):
            if(arr[i] == arr[j]):
                count += 1
        if(count > maxcount):
            maxcount = count
            element_having_max_freq = arr[i]
    
    return element_having_max_freq


marks = []

n = int(input("enter the number of students : "))
for i in range (n):
    item  = int(input("enter Marks : "))
    if item == -1:
        break
    else :
        marks.append(item)

print(marks)

# a) The average score of class
print ("average score is ")
print(average(marks))

# b) Highest score and lowest score of class
print ("highest score is ", highest(marks))
print ("lowest score is ", lowest(marks))

# c) Count of students who were absent for the test
print ("absent in test : ",n - len(marks))

# d) Display mark with highest frequency
print ("highest frequence of : ",mostFrequent(marks))
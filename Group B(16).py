# Write a Python program to store first year percentage of students in array. Write function for
# sorting array of floating point numbers in ascending order using
# a) Selection Sort
# b) Bubble sort and display top five scores.

def swap(list, A,B):
    temp = list[A]
    list[A] = list[B]
    list[B] = temp

def bubble_sort(list):
    # counter tells us weather any change is done in the list
    count = 0
    for i in range (len(list)-1):
        if list[i] > list[i+1]:
            swap(list, i, i+1)
            print(A)
            count +=1
    # loop will be repeated if list was changed in previous iteration 
    if count == 0:
        return
    else:
        bubble_sort(list)
 
A=[]

item = input("Sample input : 1 2 3 45 4 2 336 15 4 1 31 2\nEnter List : ")
temp = item.split()
for i in temp:
	A.append(int(i))


choice = int(input("Choose One\n1. Selection Sort\n2. Bubble sort and display top five scores.\n Choice :  "))

if (choice == 1):
	for i in range(len(A)):
		
		# Find the minimum element in remaining
		# unsorted array
		min_idx = i
		for j in range(i+1, len(A)):
			if A[min_idx] > A[j]:
				min_idx = j
				
		# Swap the found minimum element with
		# the first element	
		A[i], A[min_idx] = A[min_idx], A[i]
		for i in range(len(A)):
			print(A[i],end=" ")
		print("\n")

	# Driver code to test above
	print ("array Sorted using selection sort")
	for i in range(len(A)):
		print(A[i],end=" ")

elif (choice == 2):
	
    print("sorting ...")
    bubble_sort(A)
    print("\nSorted")
    print(A)



# ways of swaping elements 

# a = 10
# b = 20
# c = 30
# print("before")
# print("a = ", a)
# print("b = ", b)
# print("c = ", c)

# a, b, c = c, b, a
# print("after")
# print("a = ", a)
# print("b = ", b)
# print("c = ", c)

	# OR

# def swap(list, a, b):
#     temp = list[a]
#     list[a] = list[b]
#     list[b] = temp


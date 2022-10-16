# Write a Python program to store first year percentage of students in array. Write
# function for sorting array of floating point numbers in ascending order using quick
# sort and display top five scores

def partition(array, low, high):

	pivot = array[high]

	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])

	(array[i + 1], array[high]) = (array[high], array[i + 1])
	# print(f'Sorted array: {array}')
	return i + 1

def quick_sort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		print(f'{array}')
		quick_sort(array, low, pi - 1)
		quick_sort(array, pi + 1, high)



# Driver code
array = []
while (1):
	item = float(input("Percentage : "))
	if item == -1 : break
	array.append(item)

print("Sorting ...")
quick_sort(array, 0, len(array) - 1)

print(f'\nSorted array: {array}')

print ("Top Five : ",end="")
for i in [-1, -2, -3, -4, -5]:
	print(array[i],end=" ")	
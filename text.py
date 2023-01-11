list = []
length = int(input("list len : "))
for i in range (length):
    elem = input("element : ")
    list.append(elem)

key = input("enter element to find : ")
print(list)

left = 0
right = len(list)
mid = (left+right) // 2
found = False

while(left != right):
    mid = (left+right)//2
    if(key == list[mid]):
        print("found at ", mid, "key = ", key)
        found = True
    elif(key > list[mid]):
        left = mid+1
    elif(key < list[mid]):  
        right = mid-1

if(found == False):
    print("Not found")
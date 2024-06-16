myArray = [1, 2, 3, 4, 5, 6, 7]

# traverse through array
for i in range(len(myArray)):
    print(myArray[i])

i = 0
while i < len(myArray):
    print(myArray[i])
    i += 1

# delete from end of array
def removeEnd(arr,length):
    if length > 0:
        arr[length - 1] = 0
    else:
        print('length is zero')

# removeEnd(myArray, len(myArray))
# print(myArray)

# deletion some middle value, shift left
def removeMiddle(arr, i, length):
    for index in range(i+1, length):
        arr[index - 1] = arr[index]
    arr[length - 1] = 0

#removeMiddle(myArray, 0, len(myArray))
#print(myArray)


# insertion at end of array
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length - 1] = n

# insertEnd(myArray, 77, len(myArray), (len(myArray) +1))
# print(myArray)

# inserting at the ith index, shift right
myArray = [1, 2, 3, 4, 5, 0]
def insertMiddle(arr, i, n, length):
    for index in range(length - 1, i - 1, -1):
        arr[index] = arr[index - 1]
    arr[i] = n

insertMiddle(myArray, 1, 101, len(myArray))
print(myArray)


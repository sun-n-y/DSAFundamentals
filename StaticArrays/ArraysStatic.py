# init an array
myArray = [1, 2, 3]

# access element
#print(myArray[0])

# traverse through an array
# range returns a sequence of numbers starting 0 and increment by 1 by default
# and stops before the given number.
# for i in range(len(myArray)):
#     print(myArray[i])
#
# print(len(myArray))
#
# # or
#
# i = 0
# while i < len(myArray):
#     print(myArray[i])
#     i += 1


# deleting from end array

def removeEnd(arr, length):
    if length > 0:
        arr[length - 1] = 0
    else:
        return print('array length is 0')

# removeEnd(myArray,len(myArray))
# print(myArray)


# deleting from ith index, shifting elements to left
def removeMiddle(arr, i, length):
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]

# removeMiddle(myArray, 0, len(myArray))
# print(myArray)

# insertion at end of array

def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n
    else:
        print('no room available')

# insertEnd(myArray,100, (len(myArray)), len(myArray))
# print(myArray)

myArray = [4, 5, 6, 7, 8, 9, 10, 0]
# inserting at the ith index, shift right
def insertMiddle(arr, i, n, length):
    for index in range(length - 1, i - 1, -1):
        arr[index] = arr[index - 1]
    arr[i] = n

insertMiddle(myArray, 1, 77, len(myArray))
print(myArray)

